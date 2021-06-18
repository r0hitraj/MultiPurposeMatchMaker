# Generated by Django 3.1.4 on 2021-01-06 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Multimatch', '0009_auto_20201229_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profilepic',
        ),
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.ForeignKey(default=8055, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profilepic1',
            field=models.FileField(default='default', upload_to='profilepics1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profilepic2',
            field=models.FileField(default='8055', upload_to='profilepics2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purposedata',
            name='p_name',
            field=models.CharField(max_length=30),
        ),
    ]