.PHONY: install test run

default: test

install:
	pip install --upgrade .

test:
	PYTHONPATH=. pytest --capture=tee-sys --show-capture=stdout

run:
	@PYTHONPATH=. python converterpy/main/convert.py 60 seconds to minutes
