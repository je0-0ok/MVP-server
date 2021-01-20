# Generated by Django 2.0.13 on 2021-01-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=200, null=True)),
                ('expect', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('time', models.IntegerField(default=0)),
                ('problem', models.CharField(max_length=200, null=True)),
                ('result', models.IntegerField(default=0)),
                ('solution', models.CharField(max_length=200, null=True)),
                ('team', models.CharField(max_length=200, null=True)),
                ('level', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
