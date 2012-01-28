# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Student'
        db.create_table('school_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('school', ['Student'])

        # Adding model 'Faq'
        db.create_table('school_faq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('school', ['Faq'])

        # Adding model 'Schedule'
        db.create_table('school_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('school', ['Schedule'])

        # Adding model 'Course'
        db.create_table('school_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Schedule'])),
            ('faq', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Faq'])),
        ))
        db.send_create_signal('school', ['Course'])

        # Adding model 'Lecture'
        db.create_table('school_lecture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Course'])),
        ))
        db.send_create_signal('school', ['Lecture'])

        # Adding model 'Assignment'
        db.create_table('school_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('due', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Course'])),
        ))
        db.send_create_signal('school', ['Assignment'])

        # Adding model 'Quiz'
        db.create_table('school_quiz', (
            ('assignment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['school.Assignment'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('school', ['Quiz'])

        # Adding model 'Exercises'
        db.create_table('school_exercises', (
            ('assignment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['school.Assignment'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('school', ['Exercises'])

        # Adding model 'Question'
        db.create_table('school_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Quiz'])),
        ))
        db.send_create_signal('school', ['Question'])

        # Adding model 'AnswerableQuestion'
        db.create_table('school_answerablequestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['school.Question'], unique=True, primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('school', ['AnswerableQuestion'])

        # Adding model 'VariantQuestion'
        db.create_table('school_variantquestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['school.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('school', ['VariantQuestion'])

        # Adding model 'Variant'
        db.create_table('school_variant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('right', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.VariantQuestion'])),
        ))
        db.send_create_signal('school', ['Variant'])

        # Adding model 'Attempt'
        db.create_table('school_attempt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Student'])),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Assignment'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('points', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('school', ['Attempt'])

        # Adding model 'Announcement'
        db.create_table('school_announcement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('assignment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Course'])),
        ))
        db.send_create_signal('school', ['Announcement'])

        # Adding model 'Material'
        db.create_table('school_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lecture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Lecture'])),
        ))
        db.send_create_signal('school', ['Material'])


    def backwards(self, orm):
        
        # Deleting model 'Student'
        db.delete_table('school_student')

        # Deleting model 'Faq'
        db.delete_table('school_faq')

        # Deleting model 'Schedule'
        db.delete_table('school_schedule')

        # Deleting model 'Course'
        db.delete_table('school_course')

        # Deleting model 'Lecture'
        db.delete_table('school_lecture')

        # Deleting model 'Assignment'
        db.delete_table('school_assignment')

        # Deleting model 'Quiz'
        db.delete_table('school_quiz')

        # Deleting model 'Exercises'
        db.delete_table('school_exercises')

        # Deleting model 'Question'
        db.delete_table('school_question')

        # Deleting model 'AnswerableQuestion'
        db.delete_table('school_answerablequestion')

        # Deleting model 'VariantQuestion'
        db.delete_table('school_variantquestion')

        # Deleting model 'Variant'
        db.delete_table('school_variant')

        # Deleting model 'Attempt'
        db.delete_table('school_attempt')

        # Deleting model 'Announcement'
        db.delete_table('school_announcement')

        # Deleting model 'Material'
        db.delete_table('school_material')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'assignment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'school.answerablequestion': {
            'Meta': {'object_name': 'AnswerableQuestion', '_ormbases': ['school.Question']},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['school.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        'school.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'due': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school.attempt': {
            'Meta': {'object_name': 'Attempt'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Assignment']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.FloatField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Student']"})
        },
        'school.course': {
            'Meta': {'object_name': 'Course'},
            'faq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Faq']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Schedule']"})
        },
        'school.exercises': {
            'Meta': {'object_name': 'Exercises', '_ormbases': ['school.Assignment']},
            'assignment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['school.Assignment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'school.faq': {
            'Meta': {'object_name': 'Faq'},
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'school.lecture': {
            'Meta': {'object_name': 'Lecture'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'school.material': {
            'Meta': {'object_name': 'Material'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Lecture']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        },
        'school.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Quiz']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'school.quiz': {
            'Meta': {'object_name': 'Quiz', '_ormbases': ['school.Assignment']},
            'assignment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['school.Assignment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'school.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'school.student': {
            'Meta': {'object_name': 'Student'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'school.variant': {
            'Meta': {'object_name': 'Variant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.VariantQuestion']"}),
            'right': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'school.variantquestion': {
            'Meta': {'object_name': 'VariantQuestion', '_ormbases': ['school.Question']},
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['school.Question']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['school']
