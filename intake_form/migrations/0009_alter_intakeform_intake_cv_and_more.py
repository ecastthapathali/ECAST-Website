# Generated by Django 4.0 on 2023-06-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake_form', '0008_intakeform_intake_batch_intakeform_intake_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intakeform',
            name='intake_cv',
            field=models.FileField(blank=True, upload_to='intake_cv/'),
        ),
        migrations.AlterField(
            model_name='intakeform',
            name='intake_experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intakeform',
            name='intake_opinion',
            field=models.TextField(blank=True, null=True),
        ),
    ]