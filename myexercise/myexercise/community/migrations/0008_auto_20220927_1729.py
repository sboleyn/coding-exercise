# Generated by Django 3.2.15 on 2022-09-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_county_health_service_area_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='covid_cases_per_100k',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='county',
            name='covid_hospital_admissions_per_100k',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='county',
            name='covid_inpatient_bed_utilization',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
