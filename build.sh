source /usr/local/bin/virtualenvwrapper.sh &&
  workon objectbdd-test &&
  pip install -r requirements.txt --upgrade --force-reinstall &&
  flake8 objectbdd &&
  nosetests tests &&
  python setup.py sdist

