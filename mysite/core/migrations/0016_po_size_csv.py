# Generated by Django 3.0.4 on 2020-04-27 22:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200428_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='po_size',
            name='csv',
            field=models.FileField(default=datetime.datetime(2020, 4, 27, 22, 55, 9, 287769, tzinfo=utc), upload_to='pos/csv/'),
            preserve_default=False,
        ),
    ]
