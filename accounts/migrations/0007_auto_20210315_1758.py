# Generated by Django 3.1.7 on 2021-03-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210204_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]