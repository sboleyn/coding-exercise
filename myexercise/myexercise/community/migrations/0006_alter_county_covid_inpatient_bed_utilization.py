# Generated by Django 3.2.15 on 2022-09-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20220927_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='covid_inpatient_bed_utilization',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
