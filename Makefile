.PHONY: test develop source clean install build

develop: 
	python3 setup.py develop

source: 
	python3 setup.py sdist

build: 
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

clean:
	rm -rf dist build vin_parser.egg-info vin_parser/__pycache__

install:
	python3 setup.py install

test:
	python3 test/vin_parser_test.py

