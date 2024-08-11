# DjangoTutorial

## Introduction

Welcome to My Django Tutorials.
`Django`, a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django is known for its "batteries-included" philosophy, providing a lot of built-in features to help developers build robust web applications quickly.

This project serves as a starting point for developing a web application with Django. The instructions below will guide you through setting up the project using pipenv, a dependency manager for Python that aims to combine the best features of pip and virtualenv.


## Project Setup

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x (preferably the latest version)
- pip (Python package installer)
- pipenv (Python dependency manager)

### Installation

#### Install pipenv

```bash
pip install pipenv
```

#### Create the Django Project

```bash
django-admin startproject myproject .
```

#### Run the Development Server

Start the development server to ensure everything is set up correctly:

```bash
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000/ to see the Django welcome page.

### Directory Structure

```csharp
your-repo-name/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── Pipfile
└── Pipfile.lock 
```

## Configure pipenv Interpreter

#### Install pipenv:

```bash
pip install pipenv
```

#### Open Command Palette:

```bash 
Press Cmd + Shift + P.
Select Python Interpreter:
```

- Type Python: Select Interpreter.
- Choose the pipenv interpreter.


#### Open Integrated Terminal:

- Press Ctrl + (backtick) or go to Terminal > New Terminal.
- Activate pipenv shell if needed:

```bash
pipenv shell
```

#### Verify Setup:

Check the Python version:
```bash
python --version
```

## Create a New App

Navigate to the Project Directory

Make sure you are in the root directory of your Django project:

### Create the App

Use the startapp command to create a new app:

```bash
python manage.py startapp myapp
```

Replace myapp with the name of your new app.

### Verify Directory Structure

After running the command, you will see a new directory named myapp created within your project directory. The structure should look something like this:

```csharp
myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
├── manage.py
└── Pipfile
```

### Register the App

To make Django aware of your new app, you need to add it to the INSTALLED_APPS setting in your project's settings file (myproject/settings.py):

```python
# myproject/settings.py

INSTALLED_APPS = [
    ...
    'myapp',
]
```

## Writing Views in Django

### Basic View

A view function, or simply a view, is a Python function that takes a web request and returns a web response. This response can be HTML content, an XML document, a redirect, a 404 error, an image, or any other type of content. 

Views are usually defined in the `views.py file of your Django app`.

### Create a Basic View

Open the `views.py` file in your app directory (e.g., myapp/views.py) and define a simple view:

```python
# myapp/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
```

### Configure URLs

To map a URL to the view, you need to configure the URLconf. `Create a urls.py` file in your app directory if it doesn't exist:

```python
# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

```

Include this app’s URLs in the main urls.py file of your project:

```python
# myproject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]

```

### Run the Server

Run the development server to check if the view works correctly:

```bash
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/myapp/ to see the "Hello, world" message.

## Templates in Django

#### Create a Template Directory

Django looks for templates in a `directory named templates` inside each app. Here's how you can set up the directory structure:

Inside your app directory (e.g., myapp), create a templates directory.
Inside the templates directory, create another directory with the same name as your app. This helps to avoid template name conflicts.
Your directory structure should look like this:

```python
 myapp/
├── templates/
│   └── myapp/
│       └── index.html
├── views.py
├── urls.py
...
```

#### Create a Template

Create an HTML file inside the templates/myapp/ directory. For example, create a file named index.html:

```html
<!-- myapp/templates/myapp/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <h1>Hello, world. You're at the myapp index.</h1>
    <p>{{ message }}</p>
</body>
</html>
```

#### Update the View to Use the Template

Modify your view function to use the render function, which takes the request, the template name, and an optional context dictionary:

```py
# myapp/views.py

from django.shortcuts import render

def index(request):
    context = {
        'message': "Hello, world. You're at the myapp index with context."
    }
    return render(request, 'myapp/index.html', context)
```

<hr/>

## Connector with MySql

#### Install Connector for MySql And Django

```bash
pip install mysql-connector

pip install mysql-connector-python
```

#### Change Database in `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crmDb',
        'USER': 'root',
        'PASSWORD': 'Amey@1234',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

#### Database connection with Django

```python
import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    passwd = 'Amey1234'
)

cursorObject = database.cursor()


cursorObject.execute('CREATE DATABASE crmDb')

print("Database Connected")
```

#### Migrate database connection

```bash
python manage.py migrate
```

You can verify your database connection in `MySqlWorkbench`

## Django Authentication System

Django's authentication system provides a robust way to manage user accounts, handle login and logout, and enforce permissions and access controls.


You can create a Super User to login as Admin.

### Create a super user

- Open your terminal and navigate to your Django project directory.

```bash
python manage.py createsuperuser
```
- You will be prompted to enter a username, email address, and password.

```bash
Username (leave blank to use 'your_username'): admin
Email address: admin@example.com
Password: ********
Password (again): ********
```

- Open the Admin Interface:
    - Open your web browser and navigate to http://127.0.0.1:8000/admin/.
    - Log in using the admin username and password you set earlier.


## REST Framework in Django

Api's allow to communcate with one and another.

```bash
pip install djangorestframework
```

Let us see a complete Example of Django Rest api creation.



#### `Step 1 :` Create A new app 

```bash
django-admin startapp drinks
```


#### `Step 2 :` Register the app

- Register your app in `settings.py` and make migrations

```python
INSTALLED_APPS = [
    ...
    'drinks',
    'rest_framework',
]
```

Then, make migrations and migrate:

```bash
python manage.py makemigrations drinks
python manage.py migrate
```
#### `Step 3 :` Create and Register model

- Creating a Model named Drinks to store info about a drink 

Here is how model is created in `/drinks/models.py`

```python
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
```

Register the model in drinks/admin.py:

```python 
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)
```

### How to fetch from Api (`GET request`)

#### Create a file named `serializers.py` in your `drinks app` :

```python
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
```

#### Register your views

```python 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer

@api_view(['GET'])
def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)
```

First, configure your app's URLs in drinks/urls.py:

```python
from django.urls import path
from .views import drink_list

urlpatterns = [
    path('drinks/', drink_list),
]
```

Then, include your app's URLs in the project's urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drinks.urls')),
]
```

