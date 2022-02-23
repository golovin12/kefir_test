# Generated by Django 3.2.12 on 2022-02-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'ordering': ('date_joined',)},
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone',
            field=models.CharField(blank=True, error_messages={'unique': 'Данный номер привязан к другому аккаунту.'}, max_length=16, verbose_name='Телефон'),
        ),
    ]
