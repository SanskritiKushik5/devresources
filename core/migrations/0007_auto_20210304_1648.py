# Generated by Django 3.1.7 on 2021-03-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210304_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
