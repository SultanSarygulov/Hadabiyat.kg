from ftplib import error_temp
from django.shortcuts import render 
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Maanga, Chapter

def index(request):
    
    search_query = request.GET.get('q')

    if search_query == None:
        latest_maanga_list = Maanga.objects.order_by('-maanga_publ')[:5]
    else:
        latest_maanga_list = Maanga.objects.filter(maanga_title__icontains = search_query).order_by('-maanga_publ')
    
    return render(request, 'maangas/list.html', {'latest_maanga_list':latest_maanga_list})


def detail(request, maanga_id, chapter_id):
    try:
        a = Maanga.objects.get(id = maanga_id)
        ch = Chapter.objects.get(id = chapter_id)
    except:
        return render(request, 'maangas/error.html')

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    chapters_list = a.chapter_set.order_by('id')

    return render(request, 'maangas/detail.html', {'maanga': a,
    'chapter_id': ch.id, 
    'latest_comments_list': latest_comments_list, 
    'chapters_list': chapters_list})


def chapter(request, maanga_id, chapter_id):
    try:
        a = Maanga.objects.get(id = maanga_id)
        ch = Chapter.objects.get(id = chapter_id)
    except:
        return render(request, 'maangas/error.html')

    return render(request, 'maangas/chapter.html', {'chapter': ch, 'maanga_title': a.maanga_title})


def leave_comment(request, maanga_id):
    try:
        a = Maanga.objects.get(id = maanga_id)
    except:
        return render(request, 'maangas/error.html')

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('maangas:detail', args = (a.id,)))


