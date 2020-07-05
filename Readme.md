# Python Django on Azure Tutorial 
In this tutorial I am going to demonstrate how to develop a cloud native Django web application that leverages the Azure services such as `Storage account`, `Azure Database for PostgreSQL`, `App Service Web App`, `Application insights`, `Azure Container Registry` and `Azure DevOps`. We will use the `Storage blob service` for serving the static and media files for your Django Web App and `Azure Database for PostgreSQL` for database migrations. We will deploy the application as a Docker container into `App Service Web App` using the `Azure DevOps`. Azure DevOps uses the build pipeline to build and push the image to the `Azure Container Registry` (ACR) and a release pipeline to enable the Continues Deployment to the Web App.

## Prerequisites 
* Python 3.6 or later
* Visual Studio Code
* Python Extension for VS Code
* Azure Subscription
* Azure CLI 2.x
* Azure DevOps account

## Setting up the project
-------------
To start with the tutorial, I am using a precreated Django Web Application that contains a set of web pages. You can also clone or download the project from the [python-on-azure](https://github.com/sonusathyadas/python-on-azure). Download the project and open with Visual Studio Code.

You can now create a Python virtual environment for the application to run the application in an isolated mode. You can install the dependencies for this project within the virtual environment. Follow the steps to setup the Virual environment for yourr Django project in VS Code:
1) Open `Integrated Terminal` in VS Code and run the following command to create a virtual environment. Ensure the project root folder is set as the current directory. (Note: In root folder the `manage.py` file is located)
	> `python -m venv env`
2) Close the `Integrated Terminal` after the virtual environment is created. 
3) Open the Command Palette (View > Command Palette or (Ctrl+Shift+P). Then select the `Python: Select Interpreter command`:
4) It lists the available Python interpreters in the current environment. It lists globally installed python and virtual environment python in `env` folder. Select the virtual env python. (`eg: .\env\Scripts\Python.exe`)
5) Open the integrated terminal .Ensure the default terminal type is `Command Prommpt`. It activates the Python environment using the activation script automatically.
6) Install `Django`, `django-bootstrap4` and `Pillow` packages in the virtual environment by running one of the following commands in the VS Code Terminal:	
	> pip install django django-bootstrap4 Pillow
7) You can now run the following commands to enable database migrations using the default `sqlite3`.
    > python manage.py makemigrations contactmanager

    > python manage.py migrate

8) Run the application by running the command:
    > python manage.py runserver

9) Open browser and navigate to http://localhost:8000.

## Configure Azure Database for PostgreSQL for database 
In our application, Django uses Sqlite as the default database for user tables and admin tables. When you plan to migrate your application to Azure, you also need to think about database migrations. Sqlite is good for local development and test purposes but not good for production. So we can think of any cloud based open-source database solutions. Azure provides open-source database solutions for PostgreSQL, MySQL and MariaDB. In this tutorials we will be using `Azure Database for PostgreSQL` for out database requirements. Perform the following steps to configure `Azure Database for PostgreSQL` in our application.

1) Open the command prompt and login to your Azure subscription. Run the following command to login to your Azure subscription.
    > az login
2) Create a new Azure resource group. Execute the following command to create a resource group.
    > az group create -n AzurePythonGroup -l eastus
3) Create a new `Azure Database for PostgreSQL` instance by running the following command. Replace the **YOUR_PASSWORD** with your database server password.
    > az postgres server create  -n contactdbserver  -g AzurePythonGroup  -l eastus  --admin-user labuser  --admin-password <YOUR_PASSWORD>  --sku-name GP_Gen5_2 
4) Execute the following command to create a firewall rule to allow connections to the PostgreSQL server from all IPs. 
    > az postgres server firewall-rule create --server contactdbserver  -g AzurePythonGroup -n AllowAllIps --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255
5) Run the following command to get the server DNS name and login username.
    > az postgres server show -g AzurePythonGroup --name contactdbserver --query fullyQualifiedDomainName
    
    > az postgres server show -g AzurePythonGroup --name contactdbserver --query administratorLogin
6) You can use any PostgreSQL client tool to connect to the newly created database. You can use either `psql.exe` or `PgAdmin` to connect to the database server. Create a new database with the name `contactdb`. You can use the `fullyQualifiedDomainName` of the server as host name and `administratorLogin` value along with server name as username. For example, if login name is `labuser` and server name is `contactdbserver` then you can use `labuser@contactdbserver` as the login user name.
7) In our application, we need to install the Postgres pip package to connect to Postgres server. To install the postgres database package run the following command.
    > pip install psycopg2
8) Create a new file `envconfig.py` in the project root folder (next to manage.py) and define a method that configure the environment variables required for the application. Add the following code to the `envconfig.py` file. Replace *<YOUR_PASSWORD>* with your database password value.
    ```
    import os
    
    def set_env_variables():
        # PostgreSQL server configuration
        os.environ['DATABASE_ENGINE'] = 'django.db.backends.postgresql'
        os.environ['DATABASE_NAME'] = 'contactdb'
        os.environ['DATABASE_USERNAME'] = 'labuser@contactdbserver'
        os.environ['DATABASE_PASSWORD'] = '<YOUR_PASSWORD>'
        os.environ['DATABASE_HOST'] = 'contactdbserver.postgres.database.azure.com'
        os.environ['DATABASE_PORT'] = '5432'
    ```
9) Open the `settings.py` from the `contactproject` directory and add the following code to the import section
    ```
    from envconfig import set_env_variables
    ```
10) After the import statements add the following code to call the `set_env_variables` method to set the evironment variables.
    ```
    set_env_variables()
    ```
11) Find and replace the `DATABASES` section with the following value in the `settings.py` file.
    ```
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASE_ENGINE'),
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USERNAME'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': os.environ.get('DATABASE_PORT'),
        }
    }
    ```


## Configure Storage accout for static and media files