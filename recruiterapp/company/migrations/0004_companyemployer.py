# Generated by Django 4.1.4 on 2022-12-26 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0003_alter_company_verified_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='Recruiter', max_length=32)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
