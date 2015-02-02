source /usr/local/bin/virtualenvwrapper.sh >> log/virtualenv.log &&
  workon objectbdd-test &&
  pip install -r requirements.txt --upgrade --force-reinstall >> log/install.log &&
  ./scripts/test.sh &&
  python setup.py sdist >> log/build.log
