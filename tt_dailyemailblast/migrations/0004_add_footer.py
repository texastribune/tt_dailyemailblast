# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DailyEmailBlastType.footer'
        db.add_column('tt_dailyemailblast_dailyemailblasttype', 'footer',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DailyEmailBlastType.footer'
        db.delete_column('tt_dailyemailblast_dailyemailblasttype', 'footer')


    models = {
        'tt_dailyemailblast.dailyemailblast': {
            'Meta': {'ordering': "('-created_on',)", 'object_name': 'DailyEmailBlast'},
            'blast_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blasts'", 'to': "orm['tt_dailyemailblast.DailyEmailBlastType']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient_lists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'blasts'", 'symmetrical': 'False', 'to': "orm['tt_dailyemailblast.RecipientList']"}),
            'send_completed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'sent_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tt_dailyemailblast.dailyemailblasttype': {
            'Meta': {'object_name': 'DailyEmailBlastType'},
            'footer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tt_dailyemailblast.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tt_dailyemailblast.recipientlist': {
            'Meta': {'object_name': 'RecipientList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lists'", 'symmetrical': 'False', 'to': "orm['tt_dailyemailblast.Recipient']"})
        }
    }

    complete_apps = ['tt_dailyemailblast']