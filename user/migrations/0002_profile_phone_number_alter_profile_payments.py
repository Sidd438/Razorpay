# Generated by Django 4.0 on 2022-01-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Payments',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
