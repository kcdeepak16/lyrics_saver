from django.shortcuts import render

# Create your views here.

def home_page(request):
    if request.method == "POST":
        print(request.POST)
        return render(request, "home_page.html")
    return render(request, 'home_page.html')


import lyricsgenius
import json
token="ojBr5rlFYpe4ZOr8WTev-71TWVEacYA0Y53dGdtK-6XD-D9ghAvzx3CsQs_9jnjm"
genius = lyricsgenius.Genius(token)

artist = genius.search_artist("Gregory Alan Isakov", max_songs=3, sort="title")
song = genius.search_songs("Living Proof",per_page=10)
#print(json.dumps(song["hits"][0]["result"], indent=3))

print(song)

sl = song.lyrics
for i in sl.split("\n"):
    print(i)