# Generated by Django 5.1.1 on 2024-10-01 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="description",
            new_name="description_course",
        ),
        migrations.RenameField(
            model_name="course",
            old_name="title",
            new_name="title_course",
        ),
        migrations.RenameField(
            model_name="lesson",
            old_name="description",
            new_name="description_lesson",
        ),
        migrations.RenameField(
            model_name="lesson",
            old_name="title",
            new_name="title_lesson",
        ),
    ]
