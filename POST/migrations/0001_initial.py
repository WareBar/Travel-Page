# Generated by Django 4.2.3 on 2024-11-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=250)),
                ('banner', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]