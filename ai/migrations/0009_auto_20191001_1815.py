# Generated by Django 2.2.5 on 2019-10-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0008_rfdatamodelsecond_number_of_intrinsic_deflections_linear_v1'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfdatamodelsecond',
            name='S_avl',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rfdatamodelsecond',
            name='age',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
