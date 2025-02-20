# Database World
All database knowledge you will ever need in one single place!

## Database Managament System
Also known as DBMS, is the software resposible for creating an maintaining the database as well as the interface between users and the data. It is comprised by the database engine, the data schema and the data itself. There are 2 types; SQL DBMS and NoSQL DBMS.

- **SQL DBMS**: Also known as RDBMS, R for Relational, some examples are MSQL Server, PostgreSQL and Oracle. The data structured and unchanging. The schema is defined and consistent.
- **NoSQL DBMS**: Less structured and lacks a well defined schema, allows more flexibility. It is document-centered instead of table-centered. These type of databases are best suited for companies experiencing rapid growth or for storing large quantities of data. There are different types of NoSQL DBMS, depending on how data is stored:

1. Key-Value Store: Comprised by key value pairs, values can be anything. it is commonly used for managing shopping carts for online ecommerce. As an example, Redis.
2. Document Store: Similar to key value store systems. Keys point to documents that shared some common structure. Great choice for content management, blogs, etc. As an example, mongoDB
3. Columnar Database: Stores data in columns instead of rows, this allows scalability and fast reads. This is commonly used for big data and analytical purposes. As an example, Cassandra.
4. Graph Database: Data is interconnected and best represented as a graph. Use cases will be social media apps or recommendations. As an example, neo4j.

## Normalized vs Denormalized
Normalization is process of dividing one big table or flat tables into smaller ones looking for a reduction in redundancy and higher data integrity. Denormalization, on the other hand, is the process of doing the opposite. Transactional databases will be structured in a normalized way since it improves data writing while analitycal databases will be denormalized, hence focusing on reading speed. 

### Normal Forms
Normal forms set normalization rules. Each additional form adds another level of normalization, it goes from the First Normal Form (1NF) being the least normalized up to the Sixth Normal Form (6NF) being the most normalized approach. Most normalized databases stay in the Third Normal Form (3NF).

**First Normal Form (1NF)**
- Each record must be unique - no duplicate rows.
- Each cell must hold one value.

**Second Normal Form (2NF)**
- Must satisfy 1NF.
- Each non-key column must be dependent on all the keys.

**Third Normal Form (3NF)**
- Must satisfy 2NF.
- Non-key columns cannot depend on other non-key columns (No transitive dependencies).

## Processing Data

There are two main different systems to processing data, OLTP and OLAP.

|OLTP|OLAP|
|---|---|
|Online Transaction Processing|Online Analytical Processing|
|Normalized|Denormalized|
|Better suited for writting data|Better suited for reading data|
|Support daily transactions|Report and analyze data|
|Application oriented|Subject oriented|
|Data is considered up-to-date, operational|Data is consolidated, historical|
|Size goes up to gigabytes(smaller)|Size goes up to terabytes (bigger)|
|Simple transactional queries|Complex aggregated queries|
|Frequent updates|Limited updates|
|Several users|Few users|
|Data is stored in a Operational Database|Data is stored in a Data Warehouse|

## ETL vs ELT

Extract, Transform and Load <> Extract, Load and Transform

<p align="center">
  <img width="700" height="350" src=".attachments/etl_vs_elt.png">
</p>

## Storing Data

Data storage could be accomplished in different ways, some common ones are:

- **Structure Data**: Follows a schema, data types and relationships are defined.
- **Unstructured Data**: Schemaless, Makes up most of the data in the world.
- **Semi-structured Data**: Do not follow a larger schema, Self-describing structure (JSON, XML, etc).

### Data Lake
Central store of data for the entire organization. Contains data from different departments and sources. Stores both structured and unstructured data.

Data lakes store data as object, which means the storage is cheaper than traditional databases or data warehouses.

### Data Lakehouse
Add something here


### Data Warehouse
A computer system designed to store and analyze large amounts of data for an organization. Gathers data from different areas, integrates and stores it, making it available for analysis and dashboarding. Data is stored in a structured way, in rows and columns

### Data Mart
A relational database for analysis. It focuses on single department. There are many data marts within a data warehouse. It is just another level of segregation that helps on the organization of the data.

<p align="center">
  <img width="1041" height="377" src=".attachments/data_storage_vs.png">
</p>

## Row Storage vs Column Storage
Row storage, as its name implies, stores data by adding new rows. This is the prefereable storage approach for transactional systems since it just needs to add an additional block of data. On the other hand, data stored in a columnar approach splits columns into data block, this method is used for analytical databases as it aggregates data faster.

Compression is better on columnar storage because data of the same type is packed together, thus reducing overall size.

## Layers
Layers are all the different schemas or folders where the data is stored and organized. Most common layers are Source, Staging, Storage and Production.

Another common layer architecture is the [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture). This one is comprised by three layers: Bronze, Silver and Gold and mostly used in ELT approaches.

Layering happens in the Data Warehouse or Data Lake depening on the ETL/ELT approach.

## Partitioning
Partitioning is the process of splitting a huge table in multilpe smaller tables. This is commomnly done to increase reading performance. There are two types of partitioning, vertical, spliting by columns, and horizontal, spliting by rows.

## Table vs View vs Materialized View
- **Views**: Is the result of a stored query on the data, it is execued every time the view is run. Views do not store any data. It is just like giving a long query an alias to make it easier execute. Views are used to hide sensitive data and logic giving access to only the right data.
- **Tables**: Stores data in the database. It requieres more thinking since you have to determine relationships, data types, etc. It is useful when you are reading from it several times.
- **Materialized Views**: These views store the weury result on disk, same as a table. The difference and benefit when compared with tables is that materialized views have refresh or rematelializtion parameters that help keeping the data updated.  

## Data Warehouse Architecture 
When it comes to designing the data warehouse architecture, there are many schemas to choose from. Some of the most common aproaches are; The Inmon Model, Kimball Model, Data Vault. The business needs will highly influence the data warehouse architecture.

Process of creating a data model fo the data to be stored. Common data models are data vault or dimensional modeling. The main objective of these models is to make the reading process more efficient.

There are 3 steps when it comes to creating a model
1. Conceptual data model: Describes entities, relationships and attributes in a high level view. 
2. Logical data model: Defines tables, columns and relationships. 
3. Physical data model: Describes the physical storage. Tables are created in the database.

### Inmon Model
Designed by Bill Inmon, considered the father of the data warehouse, focuses on a Enterprise Data Warehouse, this is where all organization's data sits. Data should be cleaned before getting inside and shoudl be normalized. Data is fed into multiple data marts that serve specific departments. All naming convetions, calculations, etc are agreed upon before the creation which reduces data inaccuracy (showing two different values for the same metric). This approach is also known as the Top-down approach.

### Kimball Model
Also known as Bottom-up, Dimensional Modeling or Star Schema, the kimball approach focuses on denormalizing data into fact and dimension tables. Unlike the Inmon Model, data can be linked using shared attributes. Since models are designed on the fly, there is a higher risk of data inaccuracy.

Dimensional models are comprised by two types of tables:
- **Fact Tables**: Depend on the business case, are updated frequently and are connected to dimensions via foreign keys. This table holds all the business metrics.
- **Dimension Tables**: Hold description of attributes and does not change that often.

#### Kimball's four steps process
Four steps to build the model:
**Step 1**: Define the business process and questions the model will answer.
**Step 2**: Decide the grain. Ideally it should be the lowest posssible level, where the data cannot be split further.
**Step 3**: Identify all dimension tables, specific for the model and common ones.
**Step 4**: Identify fact tables and metrics to be added.

#### Slowly Changing Dimensions (SCD)
Different approaches to keep outdated date available for analysis. There are several types, being the type 2 the most common one.
**Type 1**: Updates the value.
**Type 2**: Adds a new record and audit columns such as valid_from and valid_to.
**Type 3**: Adds a new column with the previous value.

Furthere reading about [SCD](https://www.geeksforgeeks.org/slowly-changing-dimensions/)


**Useful links**
- Leap Frog dimensional model [videos](https://www.youtube.com/watch?v=cwpL-3rkRYQ&t)

- Create a dimensional model step by step [video](https://www.youtube.com/watch?v=7HyGM3Iw0Kc)

- Difference between Inmon and Kimball Model [video](https://www.youtube.com/watch?v=Tff34jj_V-0)

- Difference between Data Vault and Traditional Models [video](https://www.youtube.com/watch?v=D914nNWGP6E)

## :elephant: PostgresSQL

### :gear: Installation

Install PostrgeSQL by running in the terminal: 
```
sudo apt install postgresql
```

Once installed, configure users within the PostgreSQL shell. By default, the host name will be ´localhost´, port ´5432´, database name ´postgres´ and the password is empty. Add or modify user password using the ALTER command.
```
ALTER USER postgres PASSWORD 'root';
```

### :person: Roles

A role is a database object that contains information related to privileges, defining actions such as login & password, creation, read & write, etc. Rolss can be assigned to one or more users. 

There is no underlying difference between groups and users when it comes to roles. A group role 
and user role are the same object, the difference is the number of users it is assigned to. 

```
CREATE ROLE admin WITH CREATEDB CREATEROLE;
CREATE ROLE intern WITH PASSWORD 'Pass123' VALID UNTIL '2025-01-01';
```

Every user/role should have its own database for storing user information and privileges. Create a new user and its own database running the code below.

```
CREATE USER nico WITH CREATEDB LOGIN ENCRYPTED PASSWORD 'nico';
CREATE DATABASE nico;
```

### :: Privileges

Privileges are the permissions granted to users that enable them to perform certain actions, these are: SELECT , INSERT , UPDATE , DELETE , TRUNCATE , REFERENCES , TRIGGER , CREATE , CONNECT , TEMPORARY , EXECUTE , and USAGE . The privileges applicable to a particular object vary depending on the object's type (table, function, etc).


Grant privileges using the grant command
```
GRANT ALL PRIVILEGES ON DATABASE w3schools TO nico;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO nico;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO nico;
GRANT role_data_analyst TO user_nico;
```

Remove or Revoke privileges with:
```
REVOKE SELECT ON ALL TABLES IN SCHEMA public FROM nick;
REVOKE INSERT ON table_name FROM role;
```

Check given privileges by running this query:
```
SELECT grantor, grantee, table_schema, table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee = 'user_name_to_check';
```

Run PostgreSQL by typing
```
psql -U postgres -h localhost
```

List server details by running
```
SELECT * FROM pg_settings;
```

Installing pgAdmin4
This software is the helps you manage the server and its databases. It comes in two modes, desktop and web mode. Desktop mode downloads and installs an app in your machine while the web mode installs the app without any user interface, it uses the installed browser.

Install both modes or only one of them running one of the following commands:
```
sudo apt install pgadmin4
sudo apt install pgadmin4-desktop
sudo apt install pgadmin4-web
```

Once the installation process is finished, configure 
The desktop version is configured within the app while the web version is set up in the terminal running the commands below. It will ask for a user name, password (root21) and an apache configuration (answer yes). Finally it will show the url that should be used to access the system, by default it is: http://127.0.0.1/pgadmin4
```
/usr/pgadmin4/bin/setup-web.sh
```

Useful commands in PostgreSQL shell:

- \l: List of databases.
- \du: List of users and roles.
- \d: List of tables in current database.
- \dt: List of tables in current database.
- \dt+: List of tables in current database with additional info.
- \d table_name: Table information.
- \conninfo: Basic details related to the connection: user, database, port
- \q: Exit shell.

Dumping w3schools data
```
CREATE DATABASE w3schools;
\connect w3schools
\i /user_name/Documents/.../data/file.sql
```

### Postgres Admin Tables
- Information Schema
Retrieve all non-system views:
```
SELECT * FROM information_schema.views
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
```

**Useful Postgres links**
- Official Postgres Documentation: What Not to do [here](https://wiki.postgresql.org/wiki/Don%27t_Do_This)
- Postgres Useful Tips [here](https://challahscript.com/what_i_wish_someone_told_me_about_postgres)

## :duck: DuckDB
DuckDB is an in-process SQL OLAP database, which means it is a database optimized for analytics and runs within the same process as the application using it. 

Similar to SQLite, the database lives in a single file. Usual file extension are .duckdb and .db

### :gear: Installation
Install DuckDB straight from the terminal  and load data into it.
```
pip install duckdb
duckdb ~/Desktop/my_database.duckdb
CREATE TABLE duck AS SELECT * FROM read_csv('path/to/your/file.csv');
```

Load w3schools yables from the terminal:
```
duckdb my_database.duckdb -c "CREATE TABLE categories AS SELECT * FROM read_csv_auto('~/Desktop/.../categories.csv', delim=';');"
```
Information Schema stores all metadata, [official page](https://duckdb.org/docs/sql/meta/information_schema.html)

Print tables and schemas on screen by running the commands below. Default schema name is `main`
```
SELECT * FROM information_schema.tables;
SELECT * FROM information_schema.schemata;
```

You can read from parquet or csv files using the `read_parquet('filepath')` or `read_csv_auto('filepath')`

Further instructions in the [official Mother Duck page](https://motherduck.com/blog/duckdb-tutorial-for-beginners/)
