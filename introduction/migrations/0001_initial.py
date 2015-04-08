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
                ('name_en', models.CharField(max_length=55, verbose_name=b'ENG name of cat')),
                ('name_mn', models.CharField(max_length=55, verbose_name=b'MNG name of cat')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'name of the user')),
                ('email', models.CharField(max_length=50, verbose_name=b'E-mail')),
                ('subject', models.CharField(max_length=50, verbose_name=b'subject of e-mail')),
                ('message', models.TextField(verbose_name=b'text description')),
                ('sent_at', models.DateTimeField(auto_now=True, verbose_name=b'sent at')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_en', models.CharField(max_length=255, verbose_name=b'ENG name of item')),
                ('title_mn', models.CharField(max_length=255, verbose_name=b'MNG name of item')),
                ('published_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
                ('description_en', models.TextField(verbose_name=b'description')),
                ('catID', models.ForeignKey(verbose_name=b'related category', to='introduction.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(max_length=55, verbose_name=b'ENG name of menu')),
                ('name_mn', models.CharField(max_length=55, verbose_name=b'MNG name of menu')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alt', models.CharField(max_length=255, verbose_name=b'image name')),
                ('image', models.ImageField(upload_to=b'image')),
                ('infoID', models.ForeignKey(verbose_name=b'info id', to='introduction.Info')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menuID',
            field=models.ForeignKey(verbose_name=b'related menu', to='introduction.Menu'),
        ),
    ]
