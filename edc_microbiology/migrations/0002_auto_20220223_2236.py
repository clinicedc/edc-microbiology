# Generated by Django 3.2.11 on 2022-02-23 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_microbiology', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalmicrobiology',
            old_name='blood_culture_taken_date',
            new_name='blood_culture_date',
        ),
        migrations.RenameField(
            model_name='historicalmicrobiology',
            old_name='blood_culture_day_taken',
            new_name='blood_culture_day',
        ),
        migrations.RenameField(
            model_name='microbiology',
            old_name='blood_culture_taken_date',
            new_name='blood_culture_date',
        ),
        migrations.RenameField(
            model_name='microbiology',
            old_name='blood_culture_day_taken',
            new_name='blood_culture_day',
        ),
    ]