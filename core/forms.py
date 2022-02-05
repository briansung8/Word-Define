from ctypes.wintypes import WORD
from django import forms
from django.conf import settings
import requests
# This was adapted from a post by Vitor Freitas on making REST calls to Django
# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
class DictionarySearch(forms.Form):
    word= forms.CharField(max_length=80)
    def search(self):
        result = {}
        word= self.cleaned_data['word']
        endpoint= "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        url= endpoint.format(word=word)
        headers= {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        global response
        response= requests.get(url, headers=headers)
        if response.status_code == 200:
            result['success']= True
            result = response.json()
        else:
            result['success']= False
            if response.status_code == 404:
                result['message']= 'No definition for "%s"'% word
            else:
                result['message']= 'Search is not available at this time'
        return result
