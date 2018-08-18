import json
from django.http import HttpResponse
import Wallpapers.src.Services.GoogleSearchService as googleSearchService

def googleSearch(request):
    KEY_WORD = request.GET.get('KEY_WORD', '')
    response = googleSearchService.getWallpapers(KEY_WORD)
    return HttpResponse(json.dumps(response))
