# Generated by Django 3.0.4 on 2020-04-25 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_po_choose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='po',
            name='choose',
        ),
    ]
