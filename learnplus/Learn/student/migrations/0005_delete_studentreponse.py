# Generated by Django 2.2.12 on 2024-11-28 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentReponse',
        ),
    ]