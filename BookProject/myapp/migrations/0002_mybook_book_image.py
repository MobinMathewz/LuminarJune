# Generated by Django 2.2 on 2020-10-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybook',
            name='book_image',
            field=models.ImageField(default='image', upload_to='images/'),
            preserve_default=False,
        ),
    ]