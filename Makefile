build:
	docker compose build django

run__django:
	docker compose run --rm --service-ports django

shell:
	docker compose run --rm django python manage.py shell_plus

bash:
	docker compose run --rm django bash

migrate:
	docker compose run --rm django python manage.py migrate

localsuperuser:
	docker compose run --rm -e 'DJANGO_SUPERUSER_EMAIL=david@example.com' -e 'DJANGO_SUPERUSER_USERNAME=david' -e 'DJANGO_SUPERUSER_PASSWORD=Password123!' django python manage.py createsuperuser --noinput

drop_db:
	rm ./db.sqlite3
