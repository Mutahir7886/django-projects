# Generated by Django 3.0.4 on 2020-04-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20200420_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio_data',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]