# Generated by Django 4.2.1 on 2023-05-08 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customer_code_alter_customer_last_change_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='customerrole',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='customerrole',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='orgApiKey',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='orgApiKey',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='orgcustomer',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='orgcustomer',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='insert_user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='last_update_user_id',
            field=models.UUIDField(null=True),
        ),
    ]