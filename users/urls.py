from django.conf.urls import url
from users.views import UserViewSet

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

urlpatterns = [
    url(r'(?P<pk>[0-9a-f-]+)(/)?$', users_url_pk, name='user-detail'),
    url(r'', users_url, name='users'),
]
