# Generated by Django 3.0.7 on 2021-07-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snip_app', '0005_remove_snip_link_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='snip',
            name='is_encrypted',
            field=models.BooleanField(default=False),
        ),
    ]
