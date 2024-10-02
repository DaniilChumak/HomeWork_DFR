# Generated by Django 5.1.1 on 2024-10-02 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_rename_description_course_description_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите курс",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
