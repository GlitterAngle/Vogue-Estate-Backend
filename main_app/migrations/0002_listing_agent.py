# Generated by Django 5.0.2 on 2024-02-12 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='main_app.agent'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-12 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='main_app.agent'),
            preserve_default=False,
        ),
    ]
