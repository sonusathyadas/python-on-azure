# Django Tutorial - Bootstrap 4 in Django application

## Setting up Python Virtual Environment in VS Code
-------------
To create and run Django projects you can use a Virtual environment. Using a virtual environment avoids installing Django into a global Python environment and gives you exact control over the libraries used in an application. In virtual environment you can create a `requirements.txt` to reproduce files of virtual environement  to another development environment. 

Follow the steps to setup the Django project in VS Code:
1) Create a folder  "djangoweb" in your development machine. 
2) Open command prompt and set "djangoweb" as current working directory
3) Run the following command to create a virtual environment 
	> `python -m venv env`
4) Open project folder in VS code by running 
	> code .
5) In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the `Python: Select Interpreter command`:
6) It lists the available Python interpreters in the current environment. It lists globally installed python and virtual environment python in `env` folder. Select the virtual env python. (`eg: .\env\Scripts\Python.exe`)
7) Open the integrated terminal .Ensure the default terminal type is `Command Prommpt`. It activates the Python environment using the activation script automatically.
8) Install Django in the virtual environment by running one of the following commands in the VS Code Terminal:	
	> `python -m pip install django`
9) You now have a self-contained environment ready for writing Django code. VS Code activates the environment automatically when you use `Terminal: Create New Integrated Terminal`.

## Create a simple Django project
In Django terminology, a "Django project" is composed of several site-level configuration files along with one or more "apps" that you deploy to a web host to create a full web application. A Django project can contain multiple apps, each of which typically has an independent function in the project, and the same app can be in multiple Django projects.

To create a minimal Django app, then, it's necessary to first create the Django project to serve as the container for the app, then create the app itself. For both purposes, you use the Django administrative utility, `django-admin`, which is installed when you install the Django package.

1) In the VS Code Terminal where your virtual environment is activated, run the following command:
	> `django-admin startproject contactproject .`
2)  This will create new Django project with the name `contactproject`. Now you need to add a Django web app to the project.
3) Open the project in Visual Studio code. 
4) Open the VS Code Integrated Terminal. Ensure that the terminal is in virual environment. Run the following command to create a new web app in the Django project.
	```
	python manage.py startapp contactmanager
	```
5) Open the `views.py` file in the `contactmanager` application and update the content to add a method to handle the requests for home page. Add an import statement to import the `HttpResponse` from the `django.http` module.
	```
	from django.http import HttpResponse

	def home(request):
	    return HttpResponse("Hello, Django!")
	```
6) Create a new file in `contactmanager` folder with the name `urls.py`. The `urls.py` file is where you specify patterns to route different URLs to their appropriate views. The code below contains one route to map root URL of the app ("") to the views.home function that you just added to `contactmanager/views.py`. Add the following code to `urls.py`:
	```
	from django.urls import path
	from contactmanger import views

	urlpatterns=[
    	path("", views.home)
	]
	```
7) The `contactproject` project folder also contains a `urls.py` file, which is where URL routing is actually handled. Open `contactproject/urls.py` and modify it to match the following code. This code pulls in the app's `contactproject/urls.py` using `django.urls.include`, which keeps the app's routes contained within the app. This separation is helpful when a project contains multiple apps.
	```
	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
    	path('admin/', admin.site.urls),
    	path('', include('contactmanager.urls'))
	]
	```
8) In the VS Code Terminal, again with the virtual environment activated, run the development server with `python manage.py runserver` and open a browser to `http://127.0.0.1:8000/` to see a page that renders "Hello, Django".

## Using templates to render the views with Bootstrap4

1) In you web application you can configure the `bootstrap 4` for adding theming for your templates. To configure the `Bootstrap 4` in your application, install the `django-bootstrap4` using the `pip` command.
    ```
    pip install django-bootstrap4
    ```
2) Add `bootstrap4` in the `INSTALLED_APPS` list of the `settings.py` file of your project. Also add the `contactmanager` web app in the `INSTALLED_APPS` list.
    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'bootstrap4',
        'contactmanager'
    ]
    ```
3) Inside the `contactmanager` folder, create a folder named `templates` and a subfolder with the name `contactmanager` that matches the application name. Create a new html file with the name `layout.html` in the `templates\contactmanager` folder. Add the following code in the layout file. 
    ```
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <title>{% block title %}{% endblock %}</title>
        {% load static %}
        {# Load the tag library #}
        {% load bootstrap4 %}

        {# Load CSS and JavaScript #}
        {% bootstrap_css %}
        {% bootstrap_javascript jquery='full' %}
    </head>

    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="{% url 'home' %}">Contacts Manager</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'home' %}">Home</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container">
            {% block content %}
            {% endblock %}
            <hr />
        </div>
    </body>

    </html>
    ```
4) In the `templates\contactmanager` folder, create a file named `home.html` with the contents below. 
	```
    {% extends "contactmanager/layout.html" %}

    {% block title %}
        Contact Manager Application
    {% endblock %}

    {% block content %}
        <h2 class="text-center">Welcome to the application</h2>
    {% endblock %}
	```
4) At the top of `views.py`, add the following import statement:
	```
	from django.shortcuts import render
	```
5) Also, in `views.py` file add a new view method `home` with the following code. It uses the `render` from `django.shorcuts` module to render the view with a model object.
	```
	def home(request, name):
    	return render(request,'contactmanager/home.html')
	```
6) Open the `contactmanager\urls.py` file and add a new route to the route collection.
	```
	urlpatterns=[
    	path("", views.home, name="home"),    	
	]
	```
7) Run the application by running the `python manage.py runserver` command. Open browser and test the url `http://localhost:8000`.

## Serving static files
Static files are pieces of content that your web app returns as-is for certain requests, such as CSS files. Serving static files requires that the `INSTALLED_APPS` list in `settings.py` contains `django.contrib.staticfiles`, which is included by default.

1) In the project's `contactproject/urls.py`, add the following import statement:
 	```
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	 ```
2) In that same file, add the following line at the end, which includes standard static file URLs to the list that the project recognizes:
	```
	urlpatterns += staticfiles_urlpatterns()
	```
3) Create a new folder called `static` inside the `contactmanager` web app. In the `static` folder create a subfolder `contactmanager` that match the application name. Create a file named `site.css` inside `statc/contactmanager` with the following contents.
	```
	.message {
    	font-weight: 600;
    	color: blue;
	}
	```
4) In `templates/contactmanager/layout.html`, add the following lines after the `{% bootstrap_javascript jquery='full' %}`. The `{% load static %}` tag is a custom Django template tag set, which allows you to use `{% static %}` to refer to a file like the stylesheet.
	```
	{% load static %}
	<link rel="stylesheet" type="text/css" href="{% static 'contactmanager/site.css' %}" />
	```
5) Update the `templates/contactmanager/home.html` files content block with the following:
	```
    {% block content %}
    <h2 class="text-center">Welcome to the application</h2>
    <h4 class="title-text">Django web application tutorials</h4>
    {% endblock %}
	```
6) Run the application and test the url `http://localhost:8000/`

## Static files in production server
In production, Django will collect all static files from all applications in the project and put into a separate location. So we can use a dedicated static file server that improves the performance of the application. To do so, we need to run the `python manage.py collectstatic` command to put all files in to a specific location. This is required only when you deploy the application in production server, in development, we serve static files from application specific locations. 
1) In `contactproject/settings.py`, add the following line that defines a location where static files are collected when you use the collectstatic command:
	```
	 STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
	 ```
2)  The Terminal, run the command `python manage.py collectstatic` and observe that `contactmanager/site.css` is copied into the top level `static_files` folder alongside `manage.py`.
3) In practice, run `collectstatic` any time you change static files and before deploying into production.


## Using SQLServer for database migrations
A Django model is again a Python class derived from `django.db.model.Models`, which you place in the app's `models.py` file. In the database, each model is automatically given a unique ID field named `id`. All other fields are defined as properties of the class using types from `django.db.models` such as `CharField` (limited text), `TextField` (unlimited text), `EmailField`, `URLField`, `IntegerField`, `DecimalField`, `BooleanField`, `DateTimeField`, `ForeignKey` and `ManyToMany`. 

Each field takes some attributes, like `max_length`. The `blank=True` attribute means the field is optional; `null=true` means that a value is optional. There is also a `choices` attribute that limits values to values in an array of data value/display value tuples.

1) Open the `contactmanager\models.py` file and update the code with the following 
	```
    from django.db import models

    class Contact(models.Model):
        name = models.CharField(max_length=50, null=False)
        email = models.CharField(max_length=100, null=True)
        mobile = models.CharField(max_length=10, null=False)
        fax = models.CharField(max_length=20, null=True)

        def __str__(self):
            """Return the string representation """
            return f"""Name={self.name}\n
                    Email={self.email}\n
                    Mobile={self.mobile}\n
                    Fax={self.fax}"""
	```

2) By default, Django uses `sqlite` for database migrations. In this tutorial we are going to use PostgreSQL as the backend database. You can install the `psycopg2` package to connect postgresql with Django. Install the package using the following command.
    ```
    pip install psycopg2
    ```

3) Update the `DATABASES` configuration in the `settings.py`. Update the values for `HOST`, `USER` and `PASSWORD` values according to your database configuration.
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'contactdb',
            'USER': 'postgres',
            'PASSWORD': 'Password@123',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    ```
4) Open the Terminal in the virutual environment and run the following command
	> python manage.py makemigrations contactmanager
5) Run the migration command to update the model changes to database.
	> python manage.py migrate
6) You can see the migration files generated in the `migrations` folder.
