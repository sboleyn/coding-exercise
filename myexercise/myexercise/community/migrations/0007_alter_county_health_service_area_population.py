# Generated by Django 3.2.15 on 2022-09-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_alter_county_covid_inpatient_bed_utilization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='health_service_area_population',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]