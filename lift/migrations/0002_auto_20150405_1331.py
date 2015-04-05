# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lift', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='name',
            new_name='alt',
        ),
        migrations.RemoveField(
            model_name='info',
            name='image',
        ),
        migrations.AddField(
            model_name='info',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 4, 5, 13, 30, 0, 2287, tzinfo=utc), verbose_name=b'description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 4, 5, 13, 31, 36, 842274, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='published_date',
            field=models.TimeField(auto_now=True, verbose_name=b'date published'),
        ),
    ]
