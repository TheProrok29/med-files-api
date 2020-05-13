
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


MedFiles API
============

MedFilesAPI is REST implementation of `Django <https://www.djangoproject.com/>`_ system to collect personal medical data. MedFilesAPI provides a
set of `Django Rest Framework <https://www.django-rest-framework.org/>`_ views to handle basic actions such as registration, login, doctor, medicine,
med_result and more. It works with `custom user model <https://docs.djangoproject.com/en/dev/topics/auth/customizing/>`_.


Requirements
============

To be able to run **MedFilesAPI** you have to minimum meet following requirements:

- Python (3.6, 3.7, 3.8)
- Django (1.11, 2.2, 3.0)
- Django REST Framework (3.10, 3.11)
- Asgiref==3.2.7
- Certifi==2019.11.28
- Chardet==3.0.4
- Coreapi==2.3.3
- Coreschema==0.0.4
- Django-cors-headers==3.2.1
- Idna==2.9
- Itypes==1.2.0
- Jinja2==2.11.2
- MarkupSafe==1.1.1
- Pillow==7.1.2
- Python-decouple==3.3
- Pytz==2019.3
- Requests==2.23.0
- Sqlparse==0.3.1
- Uritemplate==3.0.1
- Urllib3==1.25.8

Probably on other versions of the dependency APP will also run, but I have not tested it.
All depedencys are in requirements.txt file, recomended way to install it is using python virtual environment
like `venv <https://docs.python.org/3/library/venv.html>`_ or `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ using pip install -r requirements.txt
inside virtual environment.

Optional depedencys for development purpose are in requirements-dev.txt. For example to run `codecov <https://docs.codecov.io/docs/>`_,
`coverage <https://coverage.readthedocs.io/en/coverage-5.1/>`_, git pre-commit hooks, `Sphinx <https://www.sphinx-doc.org/en/master/>`_ and more.


Installation
=============

Simply using:

.. code-block:: bash

    $ git clone git@github.com:TheProrok29/med-files-api.git
    $ cd med-files-api
    $ pip install -r requirements.txt
    $ echo >> DJANGO_SECRET_KEY='YourSecretDjangoKey' .env
    $ python manage.py runserver


Running the tests
=================

To run all authomated tests use:

.. code-block:: bash

    $ python manage.py test


Coding style
=================

I'm using `autopep8 <https://pypi.org/project/autopep8/>`_ and `flake8 <https://flake8.pycqa.org/en/latest/>`_

Documentation
=============

Documentation is under development and partially available to study at
`Read the Docs <https://med-files-api.readthedocs.io/en/latest/>`_
, also ``api/docs/`` endpoint after run application and ``docs`` directory.

Contributing
=============

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Authors
========

- **Tomasz Bogacki** - `github <https://github.com/TheProrok29/>`_

License
=============

`MIT <https://choosealicense.com/licenses/mit/>`_


Project status
===============

This is my pet project available for me and my wife to monitor ours medical history. Aplication is still under development and in future
I'll start build front-end part off this app.