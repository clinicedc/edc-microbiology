# Generated by Django 3.2.11 on 2022-02-23 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_microbiology', '0003_auto_20220223_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalmicrobiology',
            old_name='tissue_biopsy_day_taken',
            new_name='tissue_biopsy_day',
        ),
        migrations.RenameField(
            model_name='microbiology',
            old_name='tissue_biopsy_day_taken',
            new_name='tissue_biopsy_day',
        ),
    ]
