# Generated by Django 4.1.3 on 2022-11-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_rename_skills_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='skills',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='reqired_skills',
            field=models.ManyToManyField(null=True, to='mainapp.skill'),
        ),
    ]
