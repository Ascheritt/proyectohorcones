# Generated by Django 2.1.8 on 2019-10-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance_scorecard', '0032_auto_20190928_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='acumulado_kpi',
            name='meta_mensual',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
