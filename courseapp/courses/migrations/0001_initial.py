# Generated by Django 5.0.6 on 2024-05-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('imageUrl', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
