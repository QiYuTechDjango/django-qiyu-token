

test:
	cd token_app && poetry run pytest


clean-test:
	rm token_app/django_qiyu_token || true
	cd token_app && ln -s ../django_qiyu_token django_qiyu_token
	cd token_app && poetry run python manage.py migrate
	make test


run:
	cd token_app \
	    && poetry run python manage.py makemigrations \
	    && poetry run python manage.py migrate \
	    && poetry run python manage.py runserver

add-user:
	cd token_app \
	    && poetry run python manage.py createsuperuser
