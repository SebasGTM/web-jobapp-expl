# Generated by Django 4.1.3 on 2022-11-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=models.ManyToManyField(to='mainapp.skills'),
        ),
    ]