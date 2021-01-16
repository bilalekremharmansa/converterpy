.PHONY: install-local test run

default: test

python = python
twine = ${python} -m twine
pip = ${python} -m pip
pytest = ${python} -m pytest

test:
	PYTHONPATH=. ${pytest} --capture=tee-sys --show-capture=stdout

run:
	@PYTHONPATH=. ${python} converterpy/main/convert.py $(ARGS)

install-local: build-module
	${pip} uninstall -y converterpy
	${pip} install converterpy --no-index --find-links dist/

publish-stage: build-module
	@${twine} upload dist/* -r testpypi

publish-prod: build-module
	@${twine} upload dist/* -r pypi

build-module:
	rm -rf build
	rm -rf dist
	${python} setup.py sdist
	${python} setup.py bdist_wheel