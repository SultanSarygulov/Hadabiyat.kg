from ftplib import error_temp
from django.shortcuts import render 
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Maanga, Chapter

def index(request):
    
    search_query = request.GET.get('q')

    if search_query == None:
        maanga_list = Maanga.objects.order_by('-maanga_publ')
    else:
        maanga_list = Maanga.objects.filter(maanga_title__icontains = search_query).order_by('-maanga_publ')
    
    return render(request, 'maangas/list.html', {'maanga_list':maanga_list})


def detail(request, maanga_id):
    try:
        a = Maanga.objects.get(id = maanga_id)
    except:
        return render(request, 'maangas/error.html')

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    chapters_list = list(a.chapter_set.order_by('id'))

    return render(request, 'maangas/detail.html', {'maanga': a,
    'latest_comments_list': latest_comments_list,
    'chapters_list': chapters_list})


def chapter(request, maanga_id, chapter_id):
    try:
        a = Maanga.objects.get(id = maanga_id)
    except:
        return render(request, 'maangas/error.html')
    
    chapters_list = list(a.chapter_set.order_by('id'))
    all_chapters = list(Chapter.objects.all())

    chapter_num = all_chapters.index(chapters_list[chapter_id-1])+1
    
    ch = Chapter.objects.get(id = chapter_num)

    #set next and previous page
    
    ch_prev = chapter_id - 1
    ch_next = chapter_id + 1
    last_chapter = chapters_list.index(chapters_list[-1])

    return render(request, 'maangas/chapter.html', {'chapter': ch, 'maanga': a,
    'chapter_id':chapter_id,
    'prev_chapter':ch_prev,
    'next_chapter': ch_next,
    'last_chapter': last_chapter})


def leave_comment(request, maanga_id):
    try:
        a = Maanga.objects.get(id = maanga_id)
    except:
        return render(request, 'maangas/error.html')

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('maangas:detail', args = (a.id,)))


