# Generated by Django 2.2.14 on 2020-08-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_payment_is_point_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]