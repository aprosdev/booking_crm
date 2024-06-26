# Generated by Django 4.2.2 on 2023-08-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_chatroom_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='price_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='skill',
            name='supplement_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
