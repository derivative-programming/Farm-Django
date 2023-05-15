# Generated by Django 4.2.1 on 2023-05-15 08:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_plant_other_flavor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='forgot_password_key_value',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fs_user_code_value',
            field=models.UUIDField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='province',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customerrole',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='land',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='orgapikey',
            name='api_key_value',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='orgapikey',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='orgapikey',
            name='created_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='orgapikey',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='orgcustomer',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='orgcustomer',
            name='email',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='pac',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_n_var_char_val',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='tac',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='lookup_enum_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
