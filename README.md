Phidash
=======

Template project for Dash dashboards

Copy template and follow setup instructions

Run with wsgi.py. Prod server will probably need to point to wsgi.server instead of app.

Setup:
------

* Make .env file (see below)
    * IS_PROD: If True, turns debug functions off and runs public Flask test server when running wsgi.py as main
    * LOCAL_IP: Device network IP if running public Flask test server 
    * LOCAL_STORAGE_PATH: Path to the data if it is not stored in the project directory.
* Set globals in config.py
    * Set DATA_PATHS to point to pickled dataframes
    * Set project name, title and subtitle
    * If using about tab, edit contributors.
* Place data and scripts in .data
  * markdowns.py can be used to store longer text in order to keep everything clean

.env example (file is simply named '.env', not 'something.env'):
```
LOCAL_IP='192.168.0.1'
LOCAL_STORAGE_PATH='C:/Users/Me/Desktop/projectdata'
IS_PROD=False
```

Workflow:
---------

* data is loaded in .dashapp.__init__.py
  * specific data is imported by modules when needed. Never edit base DFs in callbacks!
* .dashapp.tabindex is the main page
  * import tab containers from other files (e.g. exampletab.py and abouttab.py) and update TABS variable
* Tabs should be built as modules in their own subdirectory
  * Tab components can be split into different files for more modularity

Deploy:
-------


