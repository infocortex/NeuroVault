# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import neurovault.apps.statmaps.models
import neurovault.apps.statmaps.storage


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('statmaps', '0015_auto_20141219_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atlas',
            options={'verbose_name_plural': 'Atlases'},
        ),
        migrations.AlterModelOptions(
            name='nidmresults',
            options={'verbose_name_plural': 'NIDMResults'},
        ),
        migrations.AddField(
            model_name='nidmresults',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_statmaps.nidmresults_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nidmresults',
            name='provn_file',
            field=models.FileField(upload_to=neurovault.apps.statmaps.models.upload_nidm_to, storage=neurovault.apps.statmaps.storage.NIDMStorage(), verbose_name=b'Provenance store serialization of NIDM Results (.provn)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nidmresults',
            name='ttl_file',
            field=models.FileField(storage=neurovault.apps.statmaps.storage.NIDMStorage(), upload_to=neurovault.apps.statmaps.models.upload_nidm_to, null=True, verbose_name=b'Turtle serialization of NIDM Results (.ttl)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nidmresults',
            name='zip_file',
            field=models.FileField(upload_to=neurovault.apps.statmaps.models.upload_nidm_to, storage=neurovault.apps.statmaps.storage.NIDMStorage(), verbose_name=b'NIDM Results zip file'),
            preserve_default=True,
        ),
    ]
