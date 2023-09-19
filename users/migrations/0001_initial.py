# Generated by Django 4.2.5 on 2023-09-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(default=0, editable=False, help_text='User Unique key', primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='User e-mail', max_length=254)),
                ('name', models.CharField(help_text='User Full Name', max_length=15)),
                ('password', models.CharField(help_text='User Password', max_length=20)),
            ],
            options={
                'verbose_name': '유저 정보',
                'verbose_name_plural': '유저 정보',
                'ordering': ['name'],
            },
        ),
    ]
