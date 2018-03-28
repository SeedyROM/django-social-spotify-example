from django.contrib.auth.decorators import login_required
from social_django.utils import load_strategy

def spotify_view(function):
  @login_required
  def wrap(request, *args, **kwargs):
    social = request.user.social_auth.get(provider='spotify')
    token = social.get_access_token(load_strategy())
    return function(request, token, *args, **kwargs)

  wrap.__doc__ = function.__doc__
  wrap.__name__ = function.__name__
  return wrap