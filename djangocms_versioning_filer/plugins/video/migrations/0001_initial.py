# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-12 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import djangocms_versioning_filer.fields.file
import djangocms_versioning_filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0034_remove_pagecontent_placeholders'),
        ('djangocms_versioning_filer', '0002_file_grouper'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionedVideoPlayer',
            fields=[
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('embed_link', models.CharField(blank=True, help_text='Use this field to embed videos from external services such as YouTube, Vimeo or others. Leave it blank to upload video files by adding nested "Source" plugins.', max_length=255, verbose_name='Embed link')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='video_versionedvideoplayer', serialize=False, to='cms.CMSPlugin')),
                ('poster_grouper', djangocms_versioning_filer.fields.image.ImageGrouperField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='djangocms_versioning_filer.FileGrouper', verbose_name='Poster')),
            ],
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VersionedVideoSource',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='video_versionedvideosource', serialize=False, to='cms.CMSPlugin')),
                ('text_title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('text_description', models.TextField(blank=True, verbose_name='Description')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('file_grouper', djangocms_versioning_filer.fields.file.FileGrouperField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='djangocms_versioning_filer.FileGrouper', verbose_name='File grouper')),
            ],
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VersionedVideoTrack',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='video_versionedvideotrack', serialize=False, to='cms.CMSPlugin')),
                ('kind', models.CharField(choices=[('subtitles', 'Subtitles'), ('captions', 'Captions'), ('descriptions', 'Descriptions'), ('chapters', 'Chapters')], max_length=255, verbose_name='Kind')),
                ('srclang', models.CharField(blank=True, help_text='Examples: "en" or "de" etc.', max_length=255, verbose_name='Source language')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('file_grouper', djangocms_versioning_filer.fields.file.FileGrouperField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='djangocms_versioning_filer.FileGrouper', verbose_name='File grouper')),
            ],
            bases=('cms.cmsplugin',),
        ),
    ]