# Generated by Django 5.0.2 on 2024-02-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_agent_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimage',
            name='image',
            field=models.URLField(),
        ),
    ]
