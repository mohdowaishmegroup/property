# Generated by Django 3.0.6 on 2020-12-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='users',
            name='type',
            field=models.CharField(choices=[('front_user', 'front_user'), ('supplier', 'supplier'), ('admin', 'admin')], default='admin', max_length=10),
        ),
    ]
