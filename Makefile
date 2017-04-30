.SILENT:
PYTHON=$(shell which python)
PYTEST=$(shell which py.test)

clean:
	find . \( -name *.py[co] -o -name __pycache__ \) -delete

test:
	docker-compose stop
	docker-compose run --rm -e PYTHONPATH=. web ${PYTEST} tests/

test-cov: clean
	docker-compose stop
	docker-compose run --rm -e PYTHONPATH=. web ${PYTEST} tests/ --cov=facebook -s

run: clean
	PYTHONPATH=. ${PYTHON} run.py

build:
	docker-compose stop
	docker-compose build

up:
	docker-compose stop
	docker-compose up

stop:
	docker-compose stop

web:
	docker exec -it facebook bash
