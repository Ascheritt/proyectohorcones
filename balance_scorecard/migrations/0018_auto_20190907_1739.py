# Generated by Django 2.1.8 on 2019-09-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance_scorecard', '0017_auto_20190907_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='descripcion_kpi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='info_kpi',
            name='observacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
