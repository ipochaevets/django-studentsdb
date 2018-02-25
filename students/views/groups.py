# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Groups views
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
    # return render(request, 'students/groups_list.html', {'groups': groups})
    context = {'groups': groups}
    return render(request, 'students/groups_list.html', context)

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
