# Generated by Django 4.1.4 on 2022-12-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='verified_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
