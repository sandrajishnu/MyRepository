# Generated by Django 4.1.7 on 2023-05-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('D_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Department', models.CharField(blank=True, max_length=50, null=True)),
                ('ContactN', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]