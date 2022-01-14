# Generated by Django 4.0.1 on 2022-01-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('population', models.CharField(max_length=100)),
                ('habitat', models.TextField(max_length=250)),
                ('threats', models.TextField(max_length=250)),
            ],
        ),
    ]
