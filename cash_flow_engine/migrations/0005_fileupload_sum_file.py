# Generated by Django 3.1.1 on 2020-09-13 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_flow_engine', '0004_auto_20200912_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='sum_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
