# Generated by Django 4.2.15 on 2024-09-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminn',
            name='password',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
