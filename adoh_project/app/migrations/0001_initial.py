# Generated by Django 2.2 on 2019-08-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sb1', models.IntegerField()),
                ('sb2', models.IntegerField()),
                ('sb3', models.IntegerField()),
                ('total', models.CharField(max_length=20)),
            ],
        ),
    ]