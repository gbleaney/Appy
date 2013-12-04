# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Action'
        db.delete_table(u'appy_action')

        # Adding model 'Output'
        db.create_table(u'appy_output', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Shake', max_length=25)),
        ))
        db.send_create_signal(u'appy', ['Output'])

        # Adding model 'Input'
        db.create_table(u'appy_input', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Shake', max_length=25)),
        ))
        db.send_create_signal(u'appy', ['Input'])

        # Removing M2M table for field actions on 'AppyDevice'
        db.delete_table(db.shorten_name(u'appy_appydevice_actions'))

        # Adding M2M table for field inputs on 'AppyDevice'
        m2m_table_name = db.shorten_name(u'appy_appydevice_inputs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appydevice', models.ForeignKey(orm[u'appy.appydevice'], null=False)),
            ('input', models.ForeignKey(orm[u'appy.input'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appydevice_id', 'input_id'])

        # Adding M2M table for field outputs on 'AppyDevice'
        m2m_table_name = db.shorten_name(u'appy_appydevice_outputs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appydevice', models.ForeignKey(orm[u'appy.appydevice'], null=False)),
            ('output', models.ForeignKey(orm[u'appy.output'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appydevice_id', 'output_id'])

        # Removing M2M table for field actions on 'BaseDevice'
        db.delete_table(db.shorten_name(u'appy_basedevice_actions'))

        # Adding M2M table for field inputs on 'BaseDevice'
        m2m_table_name = db.shorten_name(u'appy_basedevice_inputs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('basedevice', models.ForeignKey(orm[u'appy.basedevice'], null=False)),
            ('input', models.ForeignKey(orm[u'appy.input'], null=False))
        ))
        db.create_unique(m2m_table_name, ['basedevice_id', 'input_id'])

        # Adding M2M table for field outputs on 'BaseDevice'
        m2m_table_name = db.shorten_name(u'appy_basedevice_outputs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('basedevice', models.ForeignKey(orm[u'appy.basedevice'], null=False)),
            ('output', models.ForeignKey(orm[u'appy.output'], null=False))
        ))
        db.create_unique(m2m_table_name, ['basedevice_id', 'output_id'])


    def backwards(self, orm):
        # Adding model 'Action'
        db.create_table(u'appy_action', (
            ('isInput', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Shake', max_length=25)),
        ))
        db.send_create_signal(u'appy', ['Action'])

        # Deleting model 'Output'
        db.delete_table(u'appy_output')

        # Deleting model 'Input'
        db.delete_table(u'appy_input')

        # Adding M2M table for field actions on 'AppyDevice'
        m2m_table_name = db.shorten_name(u'appy_appydevice_actions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appydevice', models.ForeignKey(orm[u'appy.appydevice'], null=False)),
            ('action', models.ForeignKey(orm[u'appy.action'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appydevice_id', 'action_id'])

        # Removing M2M table for field inputs on 'AppyDevice'
        db.delete_table(db.shorten_name(u'appy_appydevice_inputs'))

        # Removing M2M table for field outputs on 'AppyDevice'
        db.delete_table(db.shorten_name(u'appy_appydevice_outputs'))

        # Adding M2M table for field actions on 'BaseDevice'
        m2m_table_name = db.shorten_name(u'appy_basedevice_actions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('basedevice', models.ForeignKey(orm[u'appy.basedevice'], null=False)),
            ('action', models.ForeignKey(orm[u'appy.action'], null=False))
        ))
        db.create_unique(m2m_table_name, ['basedevice_id', 'action_id'])

        # Removing M2M table for field inputs on 'BaseDevice'
        db.delete_table(db.shorten_name(u'appy_basedevice_inputs'))

        # Removing M2M table for field outputs on 'BaseDevice'
        db.delete_table(db.shorten_name(u'appy_basedevice_outputs'))


    models = {
        u'appy.appy': {
            'Meta': {'object_name': 'Appy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'New Appy'", 'max_length': '25'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'appy.appydevice': {
            'Meta': {'object_name': 'AppyDevice'},
            'appy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appy.Appy']", 'null': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appy.Device']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inputs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appy.Input']", 'symmetrical': 'False'}),
            'outputs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appy.Output']", 'symmetrical': 'False'})
        },
        u'appy.basedevice': {
            'Meta': {'object_name': 'BaseDevice'},
            'appVersion': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inputs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appy.Input']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'iPhone'", 'max_length': '15'}),
            'osVersion': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'outputs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appy.Output']", 'symmetrical': 'False'})
        },
        u'appy.device': {
            'Meta': {'object_name': 'Device'},
            'baseDevice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appy.BaseDevice']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'appy.input': {
            'Meta': {'object_name': 'Input'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Shake'", 'max_length': '25'})
        },
        u'appy.output': {
            'Meta': {'object_name': 'Output'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Shake'", 'max_length': '25'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['appy']