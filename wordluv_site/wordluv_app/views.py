import genericpath

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic

from .models import word


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

class WordDetailViewId(generic.DetailView):
    model = word
    template_name = 'wordDetail.html'

class WordDetailViewSlug(generic.DetailView):
    model = word
    template_name = 'wordDetail.html'


class WordUpdateView(UpdateView):
    model = word
    fields = ['meaning', 'examples']
    template_name = 'wordUpdate.html'

class WordDeleteView(DeleteView):
    model = word
    template_name = 'wordConfirmDelete.html'
    success_url = reverse_lazy('wordslist')