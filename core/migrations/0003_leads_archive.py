# Generated by Django 3.2.21 on 2023-10-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_leads_borthday_remove_leads_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
