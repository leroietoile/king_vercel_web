# Generated by Django 5.0.2 on 2024-06-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0012_portfolio_web_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='recollect_key',
            field=models.CharField(default='none', max_length=200),
        ),
    ]