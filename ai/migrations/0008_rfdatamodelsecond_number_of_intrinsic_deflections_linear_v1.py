# Generated by Django 2.1.10 on 2019-09-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0007_auto_20190918_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfdatamodelsecond',
            name='Number_of_intrinsic_deflections_linear_v1',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
