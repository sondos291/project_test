# Generated by Django 4.2.15 on 2024-09-04 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0002_adminn_password'),
        ('resturant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturant',
            name='admin_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminn.adminn'),
        ),
    ]
