# Generated by Django 4.0.4 on 2022-04-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('submitter', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=30)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True)),
                ('sex', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('submission_date', models.DateField()),
                ('age', models.IntegerField(null=True)),
                ('vaccinations', models.ManyToManyField(blank=True, to='adoptions.vaccine')),
            ],
        ),
    ]
