# Generated by Django 3.2.8 on 2022-03-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.CharField(max_length=2500)),
                ('image', models.ImageField(blank=True, upload_to='blog/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
