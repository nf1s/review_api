# Review it - simple review management tool

## Project overview
Simple review Management tool 

## Tasks
- Create REST API functionality to maintain a list of shipments.
- Required functionality: list, retrieve, create, update.
- Python language with utilization of Django REST framework.
- Include tests.

### Setup

Use `Python 3` for back-end

All the requirements have been described in `requirements.txt`. Make sure you add all your back-end requirements there as well!
Initial requirements include:

- [Django](https://docs.djangoproject.com/en/1.11/) as the base framework
- [djangorestframework](https://www.django-rest-framework.org/) Framework for API
- [djangorestframework-jwt](https://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework
- [django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/) for easier form layouts
- [django-filter](https://pypi.org/project/django-filter/) dynamic queryset filtering from URL parameters.
- [markdown](http://pythonhosted.org/Markdown/siteindex.html) for rendering markdown in HTML


The application uses SQLite for the database by default for simplicity reasons.

Migrate the database before the first run

    python manage.py migrate

Create a superuser

    python manage.py createsuperuser

Loading initial data for projects

    python manage.py loaddata shipments/fixtures/initial.json
 
 Running tests
    
    python manage.py test

### Running the application

    python manage.py runserver

The application should be visible at `127.0.0.1:8000` 

## Api Endpoints
    v1 - created with ViewSets and Routers
    v2 - created with class views and generics
     

    
## What has been done



## Weaknesses



