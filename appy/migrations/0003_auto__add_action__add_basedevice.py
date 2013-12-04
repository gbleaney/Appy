# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table(u'appy_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='iPhone', max_length=25)),
            ('isInput', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appy', ['Action'])

        # Adding model 'BaseDevice'
        db.create_table(u'appy_basedevice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='iPhone', max_length=15)),
            ('devVersion', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('appVersion', self.gf('django.db.models.fields.FloatField')(default=1.0)),
        ))
        db.send_create_signal(u'appy', ['BaseDevice'])

        # Adding M2M table for field actions on 'BaseDevice'
        m2m_table_name = db.shorten_name(u'appy_basedevice_actions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('basedevice', models.ForeignKey(orm[u'appy.basedevice'], null=False)),
            ('action', models.ForeignKey(orm[u'appy.action'], null=False))
        ))
        db.create_unique(m2m_table_name, ['basedevice_id', 'action_id'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table(u'appy_action')

        # Deleting model 'BaseDevice'
        db.delete_table(u'appy_basedevice')

        # Removing M2M table for field actions on 'BaseDevice'
        db.delete_table(db.shorten_name(u'appy_basedevice_actions'))


    models = {
        u'appy.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isInput': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'iPhone'", 'max_length': '25'})
        },
        u'appy.basedevice': {
            'Meta': {'object_name': 'BaseDevice'},
            'actions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appy.Action']", 'symmetrical': 'False'}),
            'appVersion': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'devVersion': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'iPhone'", 'max_length': '15'})
        }
    }

    complete_apps = ['appy']