# Generated by Django 5.1 on 2024-10-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_event_host_alter_event_guest_alter_picsrelation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
