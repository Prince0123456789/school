# Generated by Django 3.2.8 on 2022-05-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='stuent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('susername', models.CharField(max_length=20)),
                ('spassword', models.CharField(max_length=20)),
                ('sgender', models.CharField(max_length=20)),
                ('sdob', models.DateField()),
                ('smob', models.IntegerField()),
                ('sage', models.IntegerField()),
                ('sclass', models.IntegerField()),
            ],
        ),
    ]
