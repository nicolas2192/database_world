import json
import _snowflake
import streamlit as st
from snowflake.snowpark.context import get_active_session

SEMANTIC_MODEL = "@EDWH_DEV.TS_DESS_DEV.SEMANTIC_STAGE/w3_sales_model.yaml"
session = get_active_session()

st.set_page_config(page_title="W3 Sales Assistant", layout="wide")
st.title("W3Schools Sales Dashboard")


@st.cache_data(ttl=600)
def run_sql(sql: str):
    return session.sql(sql).to_pandas()


# ---------- Dashboard ----------
kpis = run_sql("""
    SELECT SUM(LINEREVENUE) AS REVENUE,
           COUNT(DISTINCT ORDERID) AS ORDERS,
           COUNT(DISTINCT CUSTOMERNAME) AS CUSTOMERS
    FROM EDWH_DEV.TS_DESS_DEV.w3_sales_v
""")
c1, c2, c3 = st.columns(3)
c1.metric("Total revenue", f"${kpis['REVENUE'][0]:,.2f}")
c2.metric("Orders", f"{kpis['ORDERS'][0]:,}")
c3.metric("Customers", f"{kpis['CUSTOMERS'][0]:,}")

left, right = st.columns(2)
with left:
    st.subheader("Monthly revenue")
    monthly = run_sql("""
        SELECT DATE_TRUNC('month', ORDERDATE) AS MONTH, SUM(LINEREVENUE) AS REVENUE
        FROM EDWH_DEV.TS_DESS_DEV.w3_sales_v GROUP BY 1 ORDER BY 1
    """)
    st.line_chart(monthly.set_index("MONTH")["REVENUE"])
with right:
    st.subheader("Revenue by category")
    cats = run_sql("""
        SELECT CATEGORYNAME, SUM(LINEREVENUE) AS REVENUE
        FROM EDWH_DEV.TS_DESS_DEV.w3_sales_v GROUP BY 1 ORDER BY 2 DESC
    """)
    st.bar_chart(cats.set_index("CATEGORYNAME")["REVENUE"])

st.divider()


# ---------- Chat with the data ----------
def ask_analyst(history):
    body = {"messages": history, "semantic_model_file": SEMANTIC_MODEL}
    resp = _snowflake.send_snow_api_request(
        "POST", "/api/v2/cortex/analyst/message", {}, {}, body, None, 50000
    )
    if resp["status"] >= 400:
        raise RuntimeError(resp["content"])
    return json.loads(resp["content"])


if "chat" not in st.session_state:
    st.session_state.chat = []      # UI messages shown on screen
    st.session_state.history = []   # messages sent to Cortex Analyst

st.subheader("Ask a question about the data")

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
        if msg.get("sql"):
            with st.expander("SQL used"):
                st.code(msg["sql"], language="sql")
        if msg.get("df") is not None:
            st.dataframe(msg["df"], use_container_width=True)

question = st.chat_input("e.g. Which country bought the most Beverages in 1996?")
if question:
    st.session_state.chat.append({"role": "user", "text": question})
    st.session_state.history.append(
        {"role": "user", "content": [{"type": "text", "text": question}]}
    )
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                result = ask_analyst(st.session_state.history)
                blocks = result["message"]["content"]
                st.session_state.history.append({"role": "analyst", "content": blocks})

                text = " ".join(b["text"] for b in blocks if b["type"] == "text")
                sql = next((b["statement"] for b in blocks if b["type"] == "sql"), None)
                df = session.sql(sql).to_pandas() if sql else None

                st.markdown(text or "Here are the results:")
                if sql:
                    with st.expander("SQL used"):
                        st.code(sql, language="sql")
                if df is not None:
                    st.dataframe(df, use_container_width=True)
                    # Simple automatic chart: first column as labels, second as values
                    if df.shape[1] == 2 and df.shape[0] > 1:
                        st.bar_chart(df.set_index(df.columns[0])[df.columns[1]])

                st.session_state.chat.append(
                    {"role": "assistant", "text": text, "sql": sql, "df": df}
                )
            except Exception as e:
                st.error(f"Could not answer that: {e}")