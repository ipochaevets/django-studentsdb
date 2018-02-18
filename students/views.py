# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Іван',
        'last_name': u'Почаєвець',
        'ticket': 2801,
        'image': 'img/ava.jpg'},
        {'id': 2,
        'first_name': u'Олександр',
        'last_name': u'Маестро',
        'ticket': 7432,
        'image': 'img/ava1.jpg'},
        {'id': 3,
        'first_name': u'Котигорошко',
        'last_name': u'Казковий',
        'ticket': 7777,
        'image': 'img/ava2.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    groups = (
        {
            'id': 1,
            'name': u'К-16',
            'leader': {
                'id': 2,
                'name': u'Маестро Олександр'
            }
        },
        {
            'id': 2,
            'name': u'К-15',
            'leader': {
                'id': 1,
                'name': u'Почаєвець Іван'
            }
        },
        {
            'id': 3,
            'name': u'К-14',
            'leader': {
                'id': 3,
                'name': u'Казковий Котигорошко'
            }
        },
    )
    # return HttpResponse('<h1>Groups Listing</h1>')
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
