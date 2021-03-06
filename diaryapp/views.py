from django.shortcuts import get_object_or_404, redirect, render
from .models import Diary

# Create your views here.

def cover(request):
    diaries = Diary.objects.all()
    num = Diary.objects.count()
    return render(request, 'cover.html',{'num':num})

def index(request):
    diaries = Diary.objects.all()
    return render(request, 'index.html', {'diaries':diaries})

def detail(request, id):
    diary = get_object_or_404(Diary, pk = id)
    return render(request, 'detail.html', {'diary':diary})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diary()
    new_diary.title = request.POST['title']
    new_diary.body = request.POST['body']
    new_diary.save()
    return redirect('detail', new_diary.id)

def edit(request, id):
    edit_diary = Diary.objects.get(id = id)
    return render(request, 'edit.html',{'diary':edit_diary})

def update(request, id):
    update_diary = Diary.objects.get(id = id)
    update_diary.title = request.POST['title']
    update_diary.body = request.POST['body']
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, id):
    delete_diary = Diary.objects.get(id = id)
    delete_diary.delete()
    return redirect('index')