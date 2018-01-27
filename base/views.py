from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        return Response({
            'leaderboard': reverse('game:leaderboard', request=request),
            'rounds': reverse('game:round', request=request),
            'questions': reverse('game:questions', request=request),
            'hints': reverse('game:hints', request=request),
            'users': reverse('users:user-list', request=request),
        })
