# Generated by Django 3.2.4 on 2021-06-10 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_qiyu_token", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bearertokenmodel",
            name="user",
            field=models.ForeignKey(
                help_text="拥有这个令牌的用户",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="用户",
            ),
        ),
    ]