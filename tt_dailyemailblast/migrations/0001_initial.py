# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipient'
        db.create_table(u'tt_dailyemailblast_recipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tt_dailyemailblast', ['Recipient'])

        # Adding model 'RecipientList'
        db.create_table(u'tt_dailyemailblast_recipientlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tt_dailyemailblast', ['RecipientList'])

        # Adding M2M table for field recipients on 'RecipientList'
        db.create_table(u'tt_dailyemailblast_recipientlist_recipients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipientlist', models.ForeignKey(orm[u'tt_dailyemailblast.recipientlist'], null=False)),
            ('recipient', models.ForeignKey(orm[u'tt_dailyemailblast.recipient'], null=False))
        ))
        db.create_unique(u'tt_dailyemailblast_recipientlist_recipients', ['recipientlist_id', 'recipient_id'])

        # Adding model 'DailyEmailBlastType'
        db.create_table(u'tt_dailyemailblast_dailyemailblasttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tt_dailyemailblast', ['DailyEmailBlastType'])

        # Adding model 'DailyEmailBlast'
        db.create_table(u'tt_dailyemailblast_dailyemailblast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blast_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blasts', to=orm['tt_dailyemailblast.DailyEmailBlastType'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tt_dailyemailblast', ['DailyEmailBlast'])

        # Adding M2M table for field recipient_lists on 'DailyEmailBlast'
        db.create_table(u'tt_dailyemailblast_dailyemailblast_recipient_lists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dailyemailblast', models.ForeignKey(orm[u'tt_dailyemailblast.dailyemailblast'], null=False)),
            ('recipientlist', models.ForeignKey(orm[u'tt_dailyemailblast.recipientlist'], null=False))
        ))
        db.create_unique(u'tt_dailyemailblast_dailyemailblast_recipient_lists', ['dailyemailblast_id', 'recipientlist_id'])


    def backwards(self, orm):
        # Deleting model 'Recipient'
        db.delete_table(u'tt_dailyemailblast_recipient')

        # Deleting model 'RecipientList'
        db.delete_table(u'tt_dailyemailblast_recipientlist')

        # Removing M2M table for field recipients on 'RecipientList'
        db.delete_table('tt_dailyemailblast_recipientlist_recipients')

        # Deleting model 'DailyEmailBlastType'
        db.delete_table(u'tt_dailyemailblast_dailyemailblasttype')

        # Deleting model 'DailyEmailBlast'
        db.delete_table(u'tt_dailyemailblast_dailyemailblast')

        # Removing M2M table for field recipient_lists on 'DailyEmailBlast'
        db.delete_table('tt_dailyemailblast_dailyemailblast_recipient_lists')


    models = {
        u'tt_dailyemailblast.dailyemailblast': {
            'Meta': {'object_name': 'DailyEmailBlast'},
            'blast_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blasts'", 'to': u"orm['tt_dailyemailblast.DailyEmailBlastType']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient_lists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'blasts'", 'symmetrical': 'False', 'to': u"orm['tt_dailyemailblast.RecipientList']"})
        },
        u'tt_dailyemailblast.dailyemailblasttype': {
            'Meta': {'object_name': 'DailyEmailBlastType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tt_dailyemailblast.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tt_dailyemailblast.recipientlist': {
            'Meta': {'object_name': 'RecipientList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lists'", 'symmetrical': 'False', 'to': u"orm['tt_dailyemailblast.Recipient']"})
        }
    }

    complete_apps = ['tt_dailyemailblast']