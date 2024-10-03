# Generated by Django 5.0.4 on 2024-10-03 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_guests_event_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventPic',
        ),
        migrations.CreateModel(
            name='EventPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/eventPictures')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='home.event')),
            ],
        ),
    ]
