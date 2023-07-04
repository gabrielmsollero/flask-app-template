# flask-app-template
Template I like to use when creating Flask applications from scratch

## Setting up virtual environment
In order to load all the dependencies of the application locally, a *virtual environment* must be created. This can be achieved by the following code:

```powershell
python -m venv venv; ./venv/Scripts/activate; pip install -r requirements.txt
```

Once created, the *venv* can be activated by running ```./venv/Scripts/activate``` and deactivated by running ```deactivate``` within the application's root folder.

## Setting up .env
The *.env* file must contain the variable ```DB_CONNECTION_STRING``` containing the MongoDB connection string. This is made so that we can simulate local databases for development, staging and production instances of the application. The *.env* file must look something like the following:
```
# .env

DB_CONNECTION_STRING=<connection_str>
```
