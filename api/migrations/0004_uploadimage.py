# Generated by Django 2.2.7 on 2020-06-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_responseapi'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='', upload_to='api/uploadedimages')),
            ],
        ),
    ]