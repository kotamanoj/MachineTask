# Generated by Django 3.2.4 on 2021-06-12 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregister',
            name='current_class',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentregister',
            name='current_session_year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentregister',
            name='previous_class',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentregister',
            name='session_year',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
