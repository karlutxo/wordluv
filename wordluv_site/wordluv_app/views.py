import genericpath
from django.shortcuts import render
from django.http import HttpResponse
from .models import word
from django.views.generic.detail import DetailView


def WordListView(request):
    searchWord = request.GET.get('searchWord')
    if searchWord:
        words = word.objects.filter(word__startswith=searchWord)
    else:
        words = word.objects.all()
    
    
    context = {
        'searchWord': searchWord,
        'words': words,
    }
    return render(request, 'wordslist.html', context)

def WordDetail(request, word_id):
    return HttpResponse("You're looking at word %s." % word_id)