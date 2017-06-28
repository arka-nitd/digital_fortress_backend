from django.conf.urls import url, include
from game.views import LeaderBoardViewSet, RoundViewSet, HintsViewSet, QuestionsViewSet, APIRoot


app_name = 'game'

leaderboard_urls = LeaderBoardViewSet.as_view(
    {
        'get': 'list'
    }
)

round_urls = RoundViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)
round_urls_pk = RoundViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    }
)

question_urls = QuestionsViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

question_urls_pk = QuestionsViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    }
)
hints_urls = HintsViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

urlpatterns = [
    url(r'leaderboard/$', leaderboard_urls, name='leaderboard'),
    url(r'rounds/$', round_urls, name='round'),
    url(r'rounds/(?P<pk>[0-9a-f-]+)(/)?$', round_urls_pk, name='round-details'),
    url(r'questions/$', question_urls, name='questions'),
    url(r'questions/(?P<pk>[0-9a-f-]+)(/)?$', question_urls_pk, name='round-details'),
    url(r'hints/$', hints_urls, name='hints'),
    url(r'', APIRoot.as_view()),
]
