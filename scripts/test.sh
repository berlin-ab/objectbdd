#!/bin/bash

source /usr/local/bin/virtualenvwrapper.sh &&
  workon objectbdd-test &&
  find . -name '*.pyc' -delete &&
  flake8 objectbdd &&
  nosetests --rednose tests
