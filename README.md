# Database World
All database knowledge you will ever need in one single place!

## :books: Data files
- w3schools database

## :elephant: PostgresSQL

Install PostrgeSQL by running in the terminal: 
```
sudo apt install postgresql
```

Once installed, configure users within the PostgreSQL shell. By default, the host name will be ´localhost´, port ´5432´, database name ´postgres´ and the password is empty. Add or modify user password using the ALTER command.
```
ALTER USER postgres PASSWORD 'root';
```

Every user/role should have its own database for storing user information and privileges. Create a new user and its own database running the code below.
```
CREATE USER nico WITH CREATEDB LOGIN ENCRYPTED PASSWORD 'nico';
CREATE DATABASE nico;

CREATE ROLE test WITH LOGIN ENCRYPTED PASSWORD 'test';
CREATE DATABASE nico;

ALTER ROLE test CREATEDB;
```

Privileges are the permissions granted to users that enable them to perform certain actions, these are: SELECT , INSERT , UPDATE , DELETE , TRUNCATE , REFERENCES , TRIGGER , CREATE , CONNECT , TEMPORARY , EXECUTE , and USAGE . The privileges applicable to a particular object vary depending on the object's type (table, function, etc).


Grant privileges using the grant command
```
GRANT ALL PRIVILEGES ON DATABASE w3schools TO nico;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO nico;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO nico;
```

Remove or Revoke privileges with:
```
REVOKE SELECT ON ALL TABLES IN SCHEMA public FROM nick;
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

**Useful Postgres links**
- Official Postgres Documentation: [What NOT to do](https://wiki.postgresql.org/wiki/Don%27t_Do_This)
- [Postgres Tips](https://challahscript.com/what_i_wish_someone_told_me_about_postgres)

