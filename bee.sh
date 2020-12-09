#!/usr/bin/sh
export PYTHONPATH=.:/usr/lib/python3/dist-packages
printenv | grep PYTHON
/usr/local/bin/behave --format=cucumber_jsonW:PrettyCucumberJSONFormatter -o target/cucumber.json 

