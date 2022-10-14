# Generated by Django 4.1.1 on 2022-10-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mob', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
