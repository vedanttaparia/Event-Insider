# Generated by Django 3.0.5 on 2020-04-26 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]