# Generated by Django 4.2.2 on 2023-07-16 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='total_for_single_event',
        ),
    ]
