# Generated by Django 4.0.3 on 2022-04-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('ph_no', models.IntegerField()),
                ('item', models.CharField(max_length=50)),
            ],
        ),
    ]
