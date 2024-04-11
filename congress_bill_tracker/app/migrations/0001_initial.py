# Generated by Django 5.0.4 on 2024-04-11 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congress', models.IntegerField()),
                ('number', models.CharField(max_length=20)),
                ('origin_chamber', models.CharField(max_length=50)),
                ('origin_chamber_code', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('bill_type', models.CharField(max_length=10)),
                ('update_date', models.DateField()),
                ('update_date_including_text', models.DateTimeField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LatestAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_date', models.DateField()),
                ('text', models.CharField(max_length=255)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='latest_action_id', to='app.bill')),
            ],
        ),
    ]