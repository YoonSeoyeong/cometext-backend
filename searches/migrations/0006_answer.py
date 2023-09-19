# Generated by Django 4.2.5 on 2023-09-18 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0005_subjectcategory_search_search_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('search_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_id', to='searches.search')),
            ],
        ),
    ]
