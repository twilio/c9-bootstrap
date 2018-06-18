#!/bin/bash -e

CONFIG_FILE = ../config.json

all: install serve

venv:
	virtualenv venv

serve:
	echo "Starting Flask server..."
	. venv/bin/activate; python run.py

install: venv dependencies configure runner

runner:
	echo '{"cmd":["make","serve"],"info":"Started $project_path$file_name","env":{},"selector":"source.ext"}' > ./.c9/runners/Bootcamp

dependencies:
	echo "Upgrading pip"
	. venv/bin/activate; pip install --upgrade pip
	echo "Resolving Python dependencies..."
	. venv/bin/activate; pip install --upgrade -r requirements.txt

configure:
	echo "Configuring app..."
	. venv/bin/activate; python configure.py $(CONFIG_FILE)
	echo "Bootstrapping app..."
	. venv/bin/activate; python bootstrap.py $(CONFIG_FILE)

clean:
	echo "Deleting configuration file..."
	rm -f $(CONFIG_FILE)
