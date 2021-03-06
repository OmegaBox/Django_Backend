# Generated by Django 2.2.14 on 2020-07-06 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0002_auto_20200706_1638'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('discount_price', models.PositiveIntegerField(blank=True, null=True)),
                ('pay_with', models.CharField(choices=[('card', '신용/체크카드'), ('phone', '휴대폰결제'), ('kakao', '카카오페이'), ('payco', '페이코')], max_length=30)),
                ('card_name', models.CharField(max_length=30)),
                ('payed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_canceled', models.BooleanField(default=False)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=20, unique=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('nonmember', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='members.NonMember')),
                ('payment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.Payment')),
            ],
        ),
    ]
