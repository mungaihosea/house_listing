# Generated by Django 3.2 on 2021-04-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharehouse_app', '0005_remove_property_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='date',
            field=models.DateField(auto_now_add=True, max_length=30, null=True),
        ),
    ]
