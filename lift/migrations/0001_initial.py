# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(max_length=255, verbose_name=b'ENG name of cat')),
                ('name_mn', models.CharField(max_length=255, verbose_name=b'MNG name of cat')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_en', models.CharField(max_length=255, verbose_name=b'ENG name of item')),
                ('title_mn', models.CharField(max_length=255, verbose_name=b'MNG name of item')),
                ('image', models.CharField(max_length=255, verbose_name=b'image name')),
                ('published_date', models.DateTimeField(verbose_name=b'date published')),
                ('catID', models.ForeignKey(verbose_name=b'related category', to='lift.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(max_length=255, verbose_name=b'ENG name of menu')),
                ('name_mn', models.CharField(max_length=255, verbose_name=b'MNG name of menu')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'image name')),
                ('infoID', models.ForeignKey(verbose_name=b'info id', to='lift.Info')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menuID',
            field=models.ForeignKey(verbose_name=b'related menu', to='lift.Menu'),
        ),
    ]
