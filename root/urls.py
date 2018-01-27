
from django.conf.urls import url, include

urlpatterns = [
    url(r'^api-admin/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('base.urls'), name="root-url"),
]
