# Generated by Django 4.2.15 on 2024-09-03 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('ready', 'Ready')], default='pending', max_length=10)),
                ('time', models.TimeField()),
                ('owner_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickupsowner', to='owner.owner')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickupsusername', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]