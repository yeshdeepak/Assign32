# Generated by Django 2.2 on 2020-03-20 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='City',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='State',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='Street_Address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='User_Role',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='Zip',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=50)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_maintenanceperson', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
