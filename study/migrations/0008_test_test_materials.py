# Generated by Django 5.1 on 2024-08-17 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0007_alter_study_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="test_materials",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="study.materials",
                verbose_name="материалы теста",
            ),
        ),
    ]
