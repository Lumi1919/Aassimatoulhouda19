# Generated by Django 3.2.2 on 2021-05-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0003_alter_audio_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
