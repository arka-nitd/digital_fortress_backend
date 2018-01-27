from django.conf.urls import url, include
from users.views import UserViewSet, LoginView, LogoutView

users_url = UserViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        )

users_url_pk = UserViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'partial_update',
            }
        )
app_name = 'users'
urlpatterns = [
    url(r'login/(?P<backend>[\w-]+)/', LoginView.as_view()),
    url(r'logout/', LogoutView.as_view()),
    url(r"(?P<pk>[0-9a-f-]+)/", users_url_pk, name='user-detail'),
    url(r'$', users_url, name='user-list'),
]
