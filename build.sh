source /usr/local/bin/virtualenvwrapper.sh &&
  workon objectbdd-test &&
  pip install -r requirements.txt --upgrade --force-reinstall &&
  ./test.sh &&
  python setup.py sdist

