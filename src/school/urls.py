from django.conf.urls.defaults import *
from school import views

urlpatterns = patterns('',
    (r'^(\w+)/$', views.home),
    (r'^(\w+)/assignments/$', views.assignments),
    (r'^(\w+)/assignment/(\d+)/$', views.assignment),
    (r'^(\w+)/attempt/feedback/$', views.attempt_feedback),#TODO: change to appropriate url
    (r'^(\w+)/video/list/$', views.video_list),
    (r'^(\w+)/progress/$', views.progress),
    (r'^(\w+)/schedule/$', views.schedule),
    (r'^(\w+)/materials/$', views.materials),
    (r'^(\w+)/faq/$', views.faq),
    (r'^(\w+)/qna/$', views.qna),
    (r'^(\w+)/preferences/$', views.preferences),
    (r'^(\w+)/change_name/$', views.change_name),
    (r'^(\w+)/change_password/$', views.change_password),
    (r'^(\w+)/change_email/$', views.change_email),
    (r'^(\w+)/change_pref/$', views.change_pref),
)
