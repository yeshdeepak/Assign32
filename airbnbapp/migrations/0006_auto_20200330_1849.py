# Generated by Django 2.2 on 2020-03-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnbapp', '0005_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='Available_Areas',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='Property_Description',
            field=models.CharField(default=' ', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='Property_Image',
            field=models.ImageField(null=True, upload_to='Images'),
        ),
    ]
