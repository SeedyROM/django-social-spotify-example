import requests
from django.http import JsonResponse
from django.shortcuts import render

from core.decorators import spotify_view


def index(request):
  return render(request, 'info/index.html')


@spotify_view
def test(request, token):
  resp = requests.get(
    'https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=3',
    headers={
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {token}'
    }
  )
  resp.raise_for_status()

  return JsonResponse({
    'token': token,
    'data': resp.json()
  })
