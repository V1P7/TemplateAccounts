# Generated by Django 4.2.4 on 2023-08-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='media/avatar.png', upload_to='media'),
        ),
    ]