

test:
	cd token_app && poetry run pytest


clean-test:
	ln -s django_qiyu_token token_app/django_qiyu_token
	cd token_app && poetry run python manage.py migrate
	make test
