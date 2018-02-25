# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Student views
def journals_list(request):
    students = (
        {'id': 1,
        'first_name': u'Іван',
        'last_name': u'Почаєвець',},
        {'id': 2,
        'first_name': u'Олександр',
        'last_name': u'Маестро',},
        {'id': 3,
        'first_name': u'Котигорошко',
        'last_name': u'Казковий',},
    )
    context = {'students': students}
    return render(request, 'students/journal.html', context)
