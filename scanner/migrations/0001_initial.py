# Generated by Django 3.1.5 on 2021-06-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('team', models.CharField(max_length=256)),
            ],
        ),
    ]
