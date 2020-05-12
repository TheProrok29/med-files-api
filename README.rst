
.. image:: https://travis-ci.org/TheProrok29/med-files-api.svg?branch=master
    :target: https://travis-ci.org/TheProrok29/med-files-api

.. image:: https://codecov.io/gh/TheProrok29/med-files-api/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/TheProrok29/med-files-api

.. image:: https://snyk.io/test/github/TheProrok29/med-files-api/badge.svg?targetFile=requirements.txt
    :target: https://snyk.io/test/github/TheProrok29/med-files-api?targetFile=requirements.txt

.. image:: https://readthedocs.org/projects/med-files-api/badge/?version=latest
    :target: https://med-files-api.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

.. image:: https://img.shields.io/codefactor/grade/github/TheProrok29/med-files-api/master?color=yellow   :alt: CodeFactor Grade



MedFiles API is REST implementation of `Django <https://www.djangoproject.com/>`_ system to collect personal medical data. MedFilesAPI provides a set of `Django Rest Framework <https://www.django-rest-framework.org/>`_ views to handle basic actions such as registration, login, doctor, medicine, med_result and more. It works with `custom user model <https://docs.djangoproject.com/en/dev/topics/auth/customizing/>`_.

Developed by Tomasz Bogacki.

Requirements
============

To be able to run **MedFilesAPI** you have to meet following requirements:

- Python (3.6, 3.7, 3.8)
- Django (1.11, 2.2, 3.0)
- Django REST Framework (3.10, 3.11)
- idna==2.9
- Psycopg2-binary==2.8.5
- Pytz==2019.3
- Requests==2.23.0
- Sqlparse==0.3.1
- Urllib3==1.25.8
- Python-decouple==3.3
- Asgiref==3.2.7
- Certifi==2019.11.28
- Chardet==3.0.4

Probably on other versions of the dependency APP will also run, but I have not tested it.
All depedency is in requirements.txt file, recomended way to install is is using python virtual environment like venv or virtualenv using pip install -r requirements inside virtual environment.

Installation and/or Contributing and development
============

Simply using:

.. code-block:: bash

    $ git clone git@github.com:TheProrok29/med-files-api.git
    $ cd med-files-api
    $ echo >> DJANGO_SECRET_KEY='YourSecretDjangoKey' .env
    $ python manage.py test
    $ python manage.py runserver

Documentation
=============

Documentation is under development and partially available to study at
`Read the Docs <https://med-files-api.readthedocs.io/en/latest/>`_
``api/docs/`` endpoint after run application and ``docs`` directory.
