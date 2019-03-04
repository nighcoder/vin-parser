.PHONY: test

develop: dist/vin_parser%.
	python3 setup.py develop

source: vin_parser
	python3 setup.py sdist

clean:
	rm -rf dist build vin_parser.egg-info

install:
	python3 setup.py install

test:
	python3 test/vin_parser_test.py

