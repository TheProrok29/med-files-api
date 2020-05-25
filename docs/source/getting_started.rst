Getting started
===============

Available endpoints
-------------------

* ``/api/user/``
* ``/api/user/me/``
* ``/api/user/token/`` (Token Based Authentication)
* ``/api/medicine/``
* ``/api/doctor/``
* ``/api/medicine/``
* ``/api/med_result/``
* ``/api/med_image/``
* ``/api/visit/``
* ``/api/tag/``


Requirements
------------

Supported authentication backends
---------------------------------

* Token based authentication from `DRF <http://www.django-rest-framework.org/api-guide/authentication#tokenauthentication>`_


Supported Python versions
-------------------------

* Python 3.6
* Python 3.7
* Python 3.8
* probably few other versions also

Supported Django versions
-------------------------

* Django 1.11
* Django 2.2
* Django 3.0
* probably few other versions also

Supported Django Rest Framework versions
----------------------------------------

* Django Rest Framework 3.10
* Django Rest Framework 3.11
* probably few other versions also


Installation
------------

Simply direct using:

.. code-block:: bash

    $ git clone git@github.com:TheProrok29/med-files-api.git
    $ cd med-files-api
    $ pip install -r requirements.txt
    $ echo >> DJANGO_SECRET_KEY='YourSecretDjangoKey' .env
    $ python manage.py runserver


It is possible also to run a dockerize version of this app, docker contains 3 images:

* Med_files_api
* Postgress database
* Pgadmin4

To use docker postgress database it is needed to change some config options:

Configure ``settings.py``:

Comment sqlite section and uncomment postgress

.. code-block:: python

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DJANGO_DB_HOST', default='db'),
        'PORT': '5432',
        }
    }

You must also add POSTGRES_USER, POSTGRES_PASSWORD, DJANGO_DB_HOST, PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD variable to .env file.

Finall step is run docker-compose
.. code-block:: bash

    $ cd med_files_api
    $ sudo docker-compose up


Running the tests
------------------

To run all automated tests use:

.. code-block:: bash

    $ python manage.py test