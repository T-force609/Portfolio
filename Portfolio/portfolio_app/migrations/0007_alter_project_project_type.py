# Generated by Django 5.1.5 on 2025-06-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_alter_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('Blender', '3D Art'), ('APP', 'Andriod App'), ('WEB', 'Web development')], max_length=7),
        ),
    ]
