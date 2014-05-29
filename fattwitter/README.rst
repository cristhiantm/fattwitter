.. 

fattwitter
======================

Quickstart
----------

To bootstrap the project::

    virtualenv fattwitter
    source fattwitter/bin/activate
    cd path/to/fattwitter/repository
    pip install -r requirements.pip
    pip install -e .
    cp fattwitter/settings/local.py.example fattwitter/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
