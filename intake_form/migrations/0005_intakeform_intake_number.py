# Generated by Django 4.0 on 2023-06-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake_form', '0004_alter_intakeform_intake_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='intakeform',
            name='intake_number',
            field=models.IntegerField(default=0),
        ),
    ]