# Review it - simple review management tool

## Project overview

Simple review Management tool

### Setup

Use `Python 3.7` for back-end

All the requirements have been described in `Pipfile`.
Docker must be installed

Initial requirements include:

- [Django](https://docs.djangoproject.com/en/1.11/) as the base framework
- [djangorestframework](https://www.django-rest-framework.org/) Framework for API
- [djangorestframework-jwt](https://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework
- [django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/) for easier form layouts
- [django-filter](https://pypi.org/project/django-filter/) dynamic queryset filtering from URL parameters.
- [markdown](http://pythonhosted.org/Markdown/siteindex.html) for rendering markdown in HTML

Add your enviroment variables in .env
flow the structure of .env.example

### Running the application

    docker-compose up --build
The application should be visible at `127.0.0.1:8000`

### Running tests
    docker-compose run web python manage.py test

###
GraphQl endpoint: /graphql
Swagger doc: /api/swagger
Redoc doc: /api/redoc

### Known bugs

drf_yasg has problems with views generating multiple api endpoints
its does not affect the functionality though
