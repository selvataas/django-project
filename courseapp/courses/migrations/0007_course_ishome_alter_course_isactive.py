# Generated by Django 5.0.6 on 2024-06-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_categories_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isHome',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
