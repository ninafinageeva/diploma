# Generated by Django 5.1 on 2024-08-17 09:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0006_question_test_answer_question_test"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="study",
            name="student",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name="студент"
            ),
        ),
    ]
