# Generated by Django 4.2.4 on 2023-09-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_forgetpassword_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='forgetpassword',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
