# Generated by Django 3.2.15 on 2022-09-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='health_service_area_population',
            field=models.IntegerField(null=True),
        ),
    ]
