import genericpath
from decouple import config
import requests
from bs4 import BeautifulSoup
import logging


from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views import generic

from .models import word

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meaning = []   
        URL = config("URL_LRBT") + self.kwargs.get('slug')
        logging.debug(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        definition_section = soup.find("section", {"id": "definitions"})
        definitions = definition_section.find_all("div", class_="d_ptma")
#        definitions = definition_section.find_all("div", class_="d_dvn")
#        logging.debug(definitions[0].prettify)
        n = 0
        for definition in definitions:
            d = definition.find("span", class_="d_dfn")
            if d is not None: 
                n += 1
                meaning.append(str(n) + ".- " + d.text.strip())
#                logging.debug(d.text.strip())
                                
            d = definition.find("span", class_="d_xpl")
            if d is not None: 
                meaning.append("    ej.- " + d.text.strip())
#                logging.debug(d.text.strip())

        context['meaning'] = '\n'.join(meaning) 
        logging.debug('\n'.join(meaning))
        return context


class WordUpdateView(UpdateView):
    model = word
    fields = ['meaning', 'examples']
    template_name = 'wordUpdate.html'

class WordDeleteView(DeleteView):
    model = word
    template_name = 'wordConfirmDelete.html'
    success_url = reverse_lazy('wordslist')

class WordCreateView(CreateView):
    model = word
    template_name = 'wordCreate.html'
    success_url = reverse_lazy('wordslist')
    fields = ['word', 'meaning', 'examples', 'slug']    