# Generated by Django 3.1.4 on 2020-12-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analystic', '0002_auto_20201228_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataentery',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
