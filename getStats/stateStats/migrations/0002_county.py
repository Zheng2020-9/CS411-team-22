# Generated by Django 3.1.7 on 2021-03-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stateStats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('name', models.CharField(help_text='Name of a US county', max_length=50)),
                ('state', models.CharField(help_text='Name of a US state or territory', max_length=40)),
                ('name_state', models.CharField(help_text='Name of a US state or territory', max_length=90, primary_key=True, serialize=False)),
                ('cases', models.IntegerField(help_text='Number of COVID-19 cases')),
                ('deaths', models.IntegerField(help_text='Number of COVID-19 deaths')),
            ],
        ),
    ]
