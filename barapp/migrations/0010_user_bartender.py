# Generated by Django 2.2.1 on 2019-07-31 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0009_cocktailingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bartender',
            field=models.BooleanField(null=True),
        ),
    ]
