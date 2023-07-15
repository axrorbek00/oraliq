# Generated by Django 4.2.3 on 2023-07-12 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('president', models.CharField(max_length=10)),
                ('aholi_soni', models.PositiveIntegerField()),
                ('mustaqilligi', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Poytaxt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('davlat', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='home.countrymodel')),
            ],
            options={
                'verbose_name': 'Poytaxt',
                'verbose_name_plural': 'Poytaxtlar',
            },
        ),
    ]
