# Generated by Django 4.2.1 on 2023-05-11 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_errorlog_is_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='errorlog',
            name='is_test',
        ),
    ]