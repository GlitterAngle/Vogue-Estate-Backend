# Generated by Django 5.0.2 on 2024-02-12 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_agent_user_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='user',
        ),
    ]
