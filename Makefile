#!/bin/bash -e

all: setup install serve

venv:
	virtualenv venv

serve:
	echo "Starting Flask server..."
	. venv/bin/activate; python run.py

install: venv dependencies runner
	@echo '@@@ INSTALL SUCCESS @@@'
	@echo '@@@ INSTALL SUCCESS @@@'
	@echo '@@@ INSTALL SUCCESS @@@'

runner:
	mkdir -p ~/workspace/.c9/runners
	touch ~/workspace/.c9/runners/Bootcamp.run
	echo '{"cmd":["make","serve"],"info":"Started $$project_path$$file_name","env":{},"selector":"source.ext"}' > ~/workspace/.c9/runners/Bootcamp.run

dependencies:
	echo "Upgrading pip"
	. venv/bin/activate; pip install --upgrade pip
	echo "Resolving Python dependencies..."
	. venv/bin/activate; pip install --upgrade -r requirements.txt
