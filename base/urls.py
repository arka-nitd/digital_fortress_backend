from django.conf.urls import url, include

from base.views import APIRoot

urlpatterns = [
    url(r'users/', include('users.urls')),
    url(r'game/', include('game.urls')),
    url(r'^$', APIRoot.as_view()),
]
