from django.conf.urls import url, include

urlpatterns = [
    url(r'users/', include('users.urls')),
    url(r'', include('game.urls')),
]
