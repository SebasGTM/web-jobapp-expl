# Generated by Django 4.1.3 on 2022-11-08 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_jobpost_expiry_alter_jobpost_required_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.author'),
        ),
    ]
