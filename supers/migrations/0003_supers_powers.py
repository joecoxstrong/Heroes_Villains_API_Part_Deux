# Generated by Django 4.0.3 on 2022-03-22 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_power_remove_supers_primary_ability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supers',
            name='powers',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='supers.power'),
        ),
    ]
