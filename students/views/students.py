# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
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
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/students_list.html', context)

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
