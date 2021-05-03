# Generated by Django 3.2 on 2021-05-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_county_vuln_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='avg_cases',
            field=models.CharField(default='', help_text='Average number of COVID-19 cases in the past week', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='county',
            name='avg_deaths',
            field=models.CharField(default='', help_text='Average number of COVID-19 deaths in the past week', max_length=10),
            preserve_default=False,
        ),
    ]
