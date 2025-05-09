# Generated by Django 5.1.3 on 2024-12-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoplayer', '0003_delete_powerpointfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('presentation_file', models.FileField(upload_to='presentations/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
