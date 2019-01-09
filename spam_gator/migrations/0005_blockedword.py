# Generated by Django 2.0 on 2018-10-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_gator', '0004_auto_20181007_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
