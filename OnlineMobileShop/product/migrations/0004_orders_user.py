# Generated by Django 2.2 on 2020-10-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201005_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.CharField(default='noname', max_length=15),
            preserve_default=False,
        ),
    ]