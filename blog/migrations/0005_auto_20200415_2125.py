# Generated by Django 3.0.5 on 2020-04-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Profit',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]