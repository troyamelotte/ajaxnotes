from django.shortcuts import render,redirect
from .models import Note
from django.http import JsonResponse
# Create your views here.

def index(request):
    notes = Note.objects.all()
    context = {
        'notes':notes,
    }
    return render(request, 'ajaxnotes/index.html', context)

def add(request):
    note = Note.objects.create(title=request.POST['name'], desc='')
    return JsonResponse({'id': note.id, 'title':note.title})

def edit(request):
    note = Note.objects.get(id=request.POST['noteid'])
    note.desc = request.POST['desc']
    note.save()
    return JsonResponse({'status':'true'})

def delete(request):
    print 'hello'*50
    note = Note.objects.get(id=request.POST['id'])
    note.delete()
    return JsonResponse({'status':'true'})
