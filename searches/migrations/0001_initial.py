# Generated by Django 4.2.5 on 2023-09-17 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('search_id', models.AutoField(default=0, editable=False, help_text='Sentence Search Key', primary_key=True, serialize=False)),
                ('sentence', models.CharField(help_text='Search Sentence', max_length=500)),
                ('search_datetime', models.DateTimeField(help_text='Search Datetime')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name': '채팅 정보',
                'verbose_name_plural': '채팅 정보',
                'ordering': ['search_datetime'],
            },
        ),
    ]
