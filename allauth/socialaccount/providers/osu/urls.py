from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import OsuProvider


urlpatterns = default_urlpatterns(OsuProvider)
