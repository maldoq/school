# Generated by Django 2.2.12 on 2024-12-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20241227_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='matieres', to='school.Classe'),
        ),
    ]
