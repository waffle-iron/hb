all: pep test

test:
	@bin/exec test

build:
	docker-compose build web

run:
	@docker-compose run --rm -p 8000:8000 web python manage.py runserver 0.0.0.0:8000

setup: createsuperuser migrate

migrate:
	@bin/exec migrate

production_dbshell:
	heroku run python manage.py dbshell --settings=hbapi.settings.heroku --app home-b

createsuperuser:
	@bin/exec createsuperuser

pep:
	@bin/docker_exec pep8 . --max-line-length=99 --count --exclude=*migrations/*.py

.PHONY: pep all test build run migrate setup createsuperuser production_dbshell
