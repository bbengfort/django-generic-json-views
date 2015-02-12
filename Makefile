# Shell to use with Make
SHELL := /bin/sh

# Set important Paths
PROJECT := genjson
LOCALPATH := $(CURDIR)/$(PROJECT)
PYTHONPATH := $(LOCALPATH)/
PYTHON_BIN := $(VIRTUAL_ENV)/bin

# Export targets not associated with files
.PHONY: test bootstrap pip virtualenv clean docs

# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf memorandi/*.egg-info

# Targets for testing
test:
	$(PYTHON_BIN)/nosetests -v tests

# Target for documentation
docs:
	cd docs
	-mkdocs build
