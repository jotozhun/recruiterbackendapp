# Generated by Django 4.1.4 on 2022-12-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='def_user', max_length=128),
        ),
    ]
