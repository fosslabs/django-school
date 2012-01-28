from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.BooleanField()

class Faq(models.Model):
    html = models.TextField()

class Schedule(models.Model):
    html = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.ForeignKey(Schedule)
    faq = models.ForeignKey(Faq)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

class LectureCategory(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)
    due = models.DateTimeField()

    def __unicode__(self):
        return self.name
    def is_viewed(self, user):
        viewed = True
        lectures = self.lecture_set.all()
        for lecture in lectures:
            if not lecture.is_viewed(user):
                viewed = False
                break
        return viewed

class Lecture(models.Model):
    name = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=100)
    course = models.ForeignKey(Course)
    category = models.ForeignKey(LectureCategory)
    recommended_literature = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    def get_users(self):
        return self.lectureattempt_set.values_list('student', flat=True)
    def is_viewed(self, user):
        return self.lectureattempt_set.count() > 0

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    due = models.DateTimeField()
    course = models.ForeignKey(Course)
    max_points = models.FloatField()
    prerequisite = models.ForeignKey(LectureCategory)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    def get_attempts(self, user):
        return self.attempt_set.filter(student=user)
    def get_users(self):
        return self.attempt_set.values_list('student', flat=True)
    @models.permalink
    def get_absolute_url(self):
        return ('school.views.assignment', [self.course.slug, str(self.id)])

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Assignment)
    variants = models.TextField()
    answer = models.CharField(max_length=30)
    explanation = models.TextField(blank=True)

class Attempt(models.Model):
    student = models.ForeignKey(User)
    assignment = models.ForeignKey(Assignment)
    date = models.DateTimeField()
    points = models.FloatField()

class LectureAttempt(models.Model):
    student = models.ForeignKey(User)
    lecture = models.ForeignKey(Lecture)
    date = models.DateTimeField()

class Announcement(models.Model):
    """Anouncement model, all anouncements will be
       displaied on course home screen"""
    date = models.DateField()
    text = models.TextField()
    assignment = models.BooleanField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.text

class Material(models.Model):
    url = models.URLField(max_length=300)
    name = models.CharField(max_length=200)
    lecture = models.ForeignKey(Lecture)

    def __unicode__(self):
        return self.name
