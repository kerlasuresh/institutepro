# Generated by Django 4.0.3 on 2022-03-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Num', models.IntegerField()),
                ('Course_Name', models.CharField(max_length=50)),
                ('Starting_time', models.TimeField(max_length=50)),
                ('Starting_Date', models.DateField(max_length=50)),
                ('Duration', models.CharField(max_length=50)),
                ('Fee', models.FloatField()),
                ('Trainer_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
