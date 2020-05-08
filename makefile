.PHONY: all prepare-dev venv lint test run shell clean build install docker
SHELL=/bin/bash

all:
	@echo "make test"
	@echo "    Run tests on project."
	@echo "make publish"
	@echo "    Installs package in your system."

test: venv
	nosetests

publish: venv
	- python setup.py sdist bdist_wheel && twine upload dist/*
