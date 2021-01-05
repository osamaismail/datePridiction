# Generated by Django 3.1.4 on 2020-12-28 07:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analystic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataentery',
            options={'verbose_name_plural': 'Data Enteries'},
        ),
        migrations.AlterField(
            model_name='dataentery',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]