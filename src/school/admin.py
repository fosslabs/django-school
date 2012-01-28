from django.contrib import admin
from django.conf import settings
from school.models import *

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class QuestionInline(admin.StackedInline):
    model = Question

class AssignmentAdmin(admin.ModelAdmin):
    inlines = [ QuestionInline, ]

class ScheduleAdmin(admin.ModelAdmin):
    class Media:
        js = ("%sschool/js/admin_textarea.js" % settings.STATIC_URL, "%sschool/js/ckeditor/ckeditor.js" % settings.STATIC_URL, "%sfilebrowser/js/FB_CKEditor.js" % settings.STATIC_URL,)

class FaqAdmin(admin.ModelAdmin):
    class Media:
        js = ("%sschool/js/admin_textarea.js" % settings.STATIC_URL, "%sschool/js/ckeditor/ckeditor.js" % settings.STATIC_URL, "%sfilebrowser/js/FB_CKEditor.js" % settings.STATIC_URL,)

admin.site.register(Student)
admin.site.register(Course, CourseAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Lecture)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Announcement)
admin.site.register(Material)
admin.site.register(Attempt)
admin.site.register(LectureCategory)
admin.site.register(LectureAttempt)
