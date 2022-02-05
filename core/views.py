from django.shortcuts import render
from .forms import DictionarySearch
# This was adapted from a post from Vitor Freitas on making REST calls to Django
# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
def dictionary1(request):
    parse= []
    search_result = {}
    if 'word' in request.GET:
        form = DictionarySearch(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionarySearch()
    return render(request, 'core/dictionary1.html', {'form': form, 'search_result': search_result})

