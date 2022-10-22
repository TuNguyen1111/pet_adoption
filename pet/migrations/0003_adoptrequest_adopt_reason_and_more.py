# Generated by Django 4.1 on 2022-10-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_adoptrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptrequest',
            name='adopt_reason',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='adoptrequest',
            name='adopter_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='adoptrequest',
            name='adopter_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adoptrequest',
            name='adopter_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='adoptrequest',
            name='adopter_last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
