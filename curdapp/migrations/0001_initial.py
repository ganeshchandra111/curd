# Generated by Django 5.0.6 on 2024-06-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=10)),
            ],
        ),
    ]