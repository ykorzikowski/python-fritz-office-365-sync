init:
	pip install -r requirements.txt

build:
	docker build . -t ykorzikowski/radiator-fritz-o365

test:
	nosetests tests
