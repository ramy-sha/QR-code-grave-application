# Generated by Django 5.0.4 on 2024-04-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullaniciicerik',
            name='icerik_dosya',
            field=models.FileField(blank=True, null=True, upload_to='kullanici_icerikleri/'),
        ),
    ]
