# Generated by Django 3.2.15 on 2022-09-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20220927_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='covid19_community_level',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=6, null=True),
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
