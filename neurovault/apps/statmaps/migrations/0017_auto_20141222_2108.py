# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('statmaps', '0016_auto_20141222_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCollectionItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('collection', models.ForeignKey(to='statmaps.Collection')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_statmaps.basecollectionitem_set', editable=False, to='contenttypes.ContentType', null=True)),
                ('tags', taggit.managers.TaggableManager(to='statmaps.KeyValueTag', through='statmaps.ValueTaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='image',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='modify_date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='description',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='modify_date',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='name',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='nidmresults',
            name='tags',
        ),
        migrations.AddField(
            model_name='image',
            name='basecollectionitem_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=999999999, serialize=False, to='statmaps.BaseCollectionItem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nidmresults',
            name='basecollectionitem_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=999999998, serialize=False, to='statmaps.BaseCollectionItem'),
            preserve_default=False,
        ),
    ]
