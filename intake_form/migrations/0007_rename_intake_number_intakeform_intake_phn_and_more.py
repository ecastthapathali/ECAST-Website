# Generated by Django 4.0 on 2023-06-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake_form', '0006_alter_intakeform_intake_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intakeform',
            old_name='intake_number',
            new_name='intake_phn',
        ),
        migrations.AddField(
            model_name='intakeform',
            name='intake_experience',
            field=models.TextField(null=True),
        ),
    ]