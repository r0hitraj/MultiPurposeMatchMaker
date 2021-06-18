# Generated by Django 3.1.4 on 2020-12-25 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Multimatch', '0004_auto_20201225_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_text', models.CharField(max_length=50)),
                ('p_image', models.FileField(upload_to='purpose_pics')),
            ],
        ),
    ]