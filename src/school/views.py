from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import check_password, User
from django.contrib import messages
from django.views.decorators.http import require_POST
from school.models import Course, Student, Assignment, Attempt
from django.core.validators import email_re
from datetime import datetime

def create_context(page, course):
    return {page: 1, 'course': course.slug, 'course_name': course.name}

@login_required
def home(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    news = course_obj.announcement_set.order_by('-date')[:3]
    c = create_context('home', course_obj)
    c['news'] = news
    return render(request, 'school/home.html', c)

@login_required
def assignments(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    assignments = course_obj.assignment_set.order_by('-pk')
    c = create_context('assignments', course_obj)
    c['assignment_list'] = assignments
    c['attempts'] = [ass.get_attempts(request.user) for ass in assignments]
    return render(request, 'school/assignment_list.html', c)

@login_required
def video_list(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    lecture_categories = course_obj.lecturecategory_set.all()
    c = create_context('video_list', course_obj)
    c['categories'] = lecture_categories
    return render(request, 'school/video_list.html', c)

def insert_assignment(category_list, assignment):
    try:
        i = category_list.index(assignment.prerequisite)
        category_list.insert(i+1, assignment)
    except ValueError:
        category_list.append(assignment)

@login_required
def progress(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    object_list = list(course_obj.lecturecategory_set.order_by('due'))
    completed_list = []
    not_completed_list = []
    for category in object_list:
        if category.is_viewed(request.user):
            completed_list.append(category)
        else:
            not_completed_list.append(category)
    assignments = course_obj.assignment_set.order_by('-due')
    for assignment in assignments:
        if assignment.get_attempts(request.user):
            insert_assignment(completed_list, assignment)
        else:
            insert_assignment(not_completed_list, assignment)
    c = create_context('progress', course_obj)
    c['completed_list'] = completed_list
    c['in_progress_list'] = not_completed_list[:4]
    c['next_up_list'] = not_completed_list[4:]
    return render(request, 'school/progress.html', c)

@login_required
def preferences(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    try:
        s = request.user.student_set.get()
    except Student.DoesNotExist:
        s = Student(user = request.user, email = False)
        s.save()
    c = create_context('preferences', course_obj)
    c['stuff_email'] = s.email
    return render(request, 'school/preferences.html', c)

@login_required
def schedule(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    schedule = course_obj.schedule
    c = create_context('schedule', course_obj)
    c['schedule_html'] = schedule.html
    return render(request, 'school/schedule.html', c)

@login_required
def faq(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    faq = course_obj.faq
    c = create_context('faq', course_obj)
    c['faq_html'] = faq.html
    return render(request, 'school/faq.html', c)

@login_required
def qna(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    c = create_context('qna', course_obj)
    return render(request, 'school/qna.html', c)

@login_required
def assignment(request, course, assignment_id):
    course_obj = get_object_or_404(Course, slug=course)
    assignment_obj = get_object_or_404(Assignment, pk=assignment_id)
    c = create_context('assignment', course_obj)
    if request.method == 'POST':
        if request.POST['action'] == 'start':
            return attempt(request, course_obj, assignment_obj)
        elif request.POST['action'] == 'end':
            return result(request, course_obj, assignment_obj)
    c['assignment'] = assignment_obj
    c['attempts_count'] = assignment_obj.get_attempts(request.user).count()
    return render(request, 'school/assignment.html', c)

def result(request, course_obj, assignment_obj):
    total = 0
    points = assignment_obj.max_points / assignment_obj.question_set.count()
    i = 1
    for question in assignment_obj.question_set.all():
        if len(question.variants.splitlines()) > 1:
            if len(question.answer.split(",")) > 1:
                v = question.variants.splitlines()
                p = question.answer.split(",")
                ans = request.POST.getlist('q'+str(i))
                correct = True
                for j in range(len(v)):
                    j += 1
                    if not (unicode(j) in p) and (unicode(j) in ans):
                        correct = False
                    elif not (unicode(j) not in p) and (unicode(j) not in ans):
                        correct = False
                if correct:

                    total += points
            else:
                if question.answer == request.POST.get('q'+str(i), -1):
                    total += points
        else:
            if question.variants == request.POST.get('q'+str(i), ""):
                total += points
        i += 1
    attempt = Attempt(student=request.user, assignment=assignment_obj, date=datetime.now(), points=total)
    attempt.save()
    c = create_context('result', course_obj)
    c['assignment'] = assignment_obj
    c['answers'] = request.POST
    c['total'] = total
    c['points'] = points
    return render(request, 'school/attempt_feedback.html', c)

def attempt(request, course_obj, assignment_obj):
    c = create_context('attempt', course_obj)
    c['assignment'] = assignment_obj
    return render(request, 'school/attempt.html', c)

@login_required
def materials(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    c = create_context('materials', course_obj)
    c['categories'] = course_obj.lecturecategory_set.order_by('due')
    return render(request, 'school/materials.html', c)

@login_required #TODO: change to appropriate
def attempt_feedback(request, course):
    course_obj = get_object_or_404(Course, slug=course)
    c = create_context('materials', course_obj)
    return render(request, 'school/attempt_feedback.html', c)

@login_required
@require_POST
def change_name(request, course):
    name = request.POST['name']
    surname = request.POST['surname']
    request.user.first_name = name
    request.user.last_name = surname
    request.user.save()
    messages.success(request, "Name and surname successfully changed", extra_tags="name")
    return redirect('school.views.preferences', course)

@login_required
@require_POST
def change_password(request, course):
    old_password = request.POST['currpass']
    new_password = request.POST['newpass']
    new_password2 = request.POST['retypepass']
    if new_password == new_password2 and check_password(old_password, request.user.password):
        if len(new_password) > 4:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password successfully changed", extra_tags="pass")
        else:
            messages.error(request, "Password must be at least 5 characters long", extra_tags="pass")
    else:
        if new_password != new_password2:
            messages.error(request, "Two passwords didn't match", extra_tags="pass")
        if not check_password(old_password, request.user.password):
            messages.error(request, "Wrong current password", extra_tags="pass")
    return redirect('school.views.preferences', course)

@login_required
@require_POST
def change_email(request, course):
    new_email = request.POST['newemail']
    new_email2 = request.POST['retypeemail']
    if new_email == new_email2:
        if is_valid_email(new_email):
            if request.user.email != new_email and User.objects.filter(email__iexact=new_email):
                messages.error(request, "This email is already in use", extra_tags="email")
            else:
                request.user.email = new_email
                request.user.save()
                messages.success(request, "Email successfully changed", extra_tags="email")
        else:
            messages.error(request, "Please enter valid email", extra_tags="email")
    else:
        messages.error(request, "Emails don't match", extra_tags="email")
    return redirect('school.views.preferences', course)

@login_required
@require_POST
def change_pref(request, course):
    email = request.POST.get('stuff_email', False)
    change = email
    try:
        s = request.user.student_set.get()
        change = bool(email) != s.email
        s.email = email
        s.save()
    except Student.DoesNotExist:
        s = Student(user = request.user, email = email)
        s.save
    if change:
        if email:
            message = "Subscribed to the announcement mailing list"
        else:
            message = "Unsubscribed from the announcement mailing list"
        messages.success(request, message, extra_tags="stuff")
    return redirect('school.views.preferences', course)

def is_valid_email(email):
    return True if email_re.match(email) else False
