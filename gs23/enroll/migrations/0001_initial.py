# Generated by Django 5.1.2 on 2024-10-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=100)),
                ('stuemail', models.EmailField(max_length=100)),
                ('stupass', models.CharField(max_length=100)),
            ],
        ),
    ]
