# Generated by Django 4.1 on 2023-12-26 23:01

from django.db import migrations, models

import imagep.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=imagep.utils.upload_to)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
