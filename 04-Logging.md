# 4. Logging

Take a look at the [Logging section](http://pywps.readthedocs.io/en/latest/configuration.html#logging)
in the configuration file. PyWPS currently logs events to two different 
locations:
1. A log file where messages are stored. The kind of messages is set in the 
configuration file.
2. A database where each request to the service is registered. 

PyWPS uses [SQLAlchemy](http://www.sqlalchemy.org/) to connect and work with 
multiple database management systems. SQLite and Postgresql tend to be the most used options

## Exercises

### 4.1. Browsing

#### 4.1.1. Finding errors

Open a command line session and move to the `pywps-flask/logs` folder.
Using the `tail` and/or `cat` commands search for error messages in the 
`pywps.log` file. 

Tip: these messages are preceded by the string "[ERROR]", it is possible to grep the error messages:

```
cat pywps.log | grep "\[ERROR\]"
```

#### 4.1.2. Continuous monitoring

Use the `tail` command to continuously monitor the activity of the service. 
Repeat some of the requests in the previous exercises to see new activity. Tip:
use `man tail` to learn more about this command.

#### 4.1.3. Database browser

If you have no database browsing programme installed, Install [DB Browser 
for SQLite](http://sqlitebrowser.org/) on your system. On Debian based systems
it can be installed from the command line: 

`sudo apt install sqlitebrowser`.

#### 4.1.4. Consult database

Start the database browser and open the PyWPS logging database, by default
the file `pywps-flask/logs/pywps-logs.sqlite3`. Either using the GUI itself or
using the SQL language, identify at which time was issued the first 
*GetCapabilities* request to the service. 

### 4.2. Reconfigure

Follow the instructions in the [SQLAlchemy documentation](http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html?highlight=postgres#module-sqlalchemy.dialects.postgresql.psycopg2) 
in order to reconfigure your server so that logging to a Postgres database. 
Tip I: if you are following this workshop on the OSGeo-Live system, [Postgres is 
already installed](https://live.osgeo.org/en/overview/postgis_overview.html).
Tip II: it might be wise to [create a new Postgres user](https://www.postgresql.org/docs/8.0/static/sql-createuser.html) 
for PyWPS.

### 4.3. Logging debug messages

Coming soon.