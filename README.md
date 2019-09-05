# Review it - simple review management tool

## Project overview

Simple review Management tool

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

### Running the application

    docker-compose up --build

The application should be visible at `0.0.0.0:8000`
