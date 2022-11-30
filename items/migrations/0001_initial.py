# Generated by Django 4.1.2 on 2022-11-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadlift', models.CharField(default=' ', max_length=300)),
                ('squat', models.CharField(default=' ', max_length=300)),
                ('bench', models.CharField(default=' ', max_length=300)),
                ('clean', models.CharField(default=' ', max_length=300)),
                ('snatch', models.CharField(default=' ', max_length=300)),
                ('ohp', models.CharField(default=' ', max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
