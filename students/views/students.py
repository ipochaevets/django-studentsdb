# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Student

# Student views
def students_list(request):
    # students = (
    #     {'id': 1,
    #     'first_name': u'Іван',
    #     'last_name': u'Почаєвець',
    #     'ticket': 2801,
    #     'image': 'img/ava.jpg'},
    #     {'id': 2,
    #     'first_name': u'Олександр',
    #     'last_name': u'Маестро',
    #     'ticket': 7432,
    #     'image': 'img/ava1.jpg'},
    #     {'id': 3,
    #     'first_name': u'Котигорошко',
    #     'last_name': u'Казковий',
    #     'ticket': 7777,
    #     'image': 'img/ava2.jpg'},
    # )
    # return render(request, 'students/students_list.html', {'students': students})
    students = Student.objects.all().order_by('last_name')
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999), deliver last page of resuls.
        students = paginator.page(paginator.num_pages)
    """
    # my pagination
    students_count = Student.objects.all().count()
    if students_count % 3:
        total_pages = (students_count / 3) + 1
    else:
        total_pages = students_count / 3
    page_tmp = request.GET.get('page', '0')
    try:
        page = int(page_tmp)
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    if page > total_pages:
        page = total_pages
    limit = 3 * page
    offset = limit - 3
    students = students[offset:limit]
    """
    context = {'students': students}
    return render(request, 'students/students_list.html', context)

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
