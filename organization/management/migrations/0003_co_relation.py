# Generated by Django 3.0.4 on 2020-04-07 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200407_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='co_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Branches')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.users')),
            ],
        ),
    ]