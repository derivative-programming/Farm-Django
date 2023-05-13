# Generated by Django 4.2.1 on 2023-05-08 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_customer_fs_user_code_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='tac_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='tac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_list', to='api.tac'),
        ),
    ]