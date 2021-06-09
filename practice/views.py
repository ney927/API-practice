from django.shortcuts import render
import requests

# Create your views here.

def thesaurus_view(request):
  def getList(code, word):
    parameter = {f"rel_{code}":word}
    request = requests.get('https://api.datamuse.com/words',parameter)
    req_json = request.json()
    words = []
    for i in req_json[0:5]:
      words.append(i['word'])
    return words
  syn = []
  ant = []
  word = ''
  if request.method=='POST':
    word = request.POST.get('word')
    syn = getList('syn', word)
    ant = getList('ant', word)
  context = {
    'syn': syn,
    'ant': ant,
    'word':word
  }
  return render(request, 'thes.html', context)
