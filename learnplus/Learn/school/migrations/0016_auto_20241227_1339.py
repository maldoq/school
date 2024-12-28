# Generated by Django 2.2.12 on 2024-12-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20241227_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='matieres',
        ),
        migrations.AlterField(
            model_name='classe',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classe_filiere', to='school.Filiere'),
        ),
        migrations.CreateModel(
            name='ClasseMatiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('classe', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classe_matieres', to='school.Classe')),
                ('matiere', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matiere_classes', to='school.Matiere')),
            ],
            options={
                'verbose_name': 'Classe Matiere',
                'verbose_name_plural': 'Classe Matieres',
                'unique_together': {('classe', 'matiere')},
            },
        ),
    ]