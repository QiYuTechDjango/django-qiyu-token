djangoRun:=cd token_app && poetry run python manage.py

# i18n 提取出翻译的字符串
i18n-extract:
	$(djangoRun) makemessages --locale en
	$(djangoRun) makemessages --locale zh


# i18n 编译翻译后的字符串
i18n-compile:
	$(djangoRun) compilemessages
