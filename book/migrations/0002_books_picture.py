# Generated by Django 4.2.6 on 2023-11-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]