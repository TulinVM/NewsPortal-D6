# Generated by Django 4.2 on 2023-04-15 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='category',
            field=models.CharField(choices=[('uncos', 'Новости'), ('articles', 'Статьи')], default='uncos', max_length=10),
        ),
    ]
