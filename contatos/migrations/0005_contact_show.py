# Generated by Django 3.2.3 on 2021-05-15 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_alter_contact_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
