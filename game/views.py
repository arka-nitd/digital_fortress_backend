from rest_framework import viewsets
from game.serializers import (
    LeaderBoardSerializer,
    RoundSerializer,
    HintSerializer,
    ListQuestionSerializer,
    CreateUpdateQuestionSerializer,
    DashboardSerializer,
    CreateUpdateRoundSerializer
)
from game.models import LeaderBoard, Round, Hint, Question
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from game.permissions import IsRoundPermitted
from rest_framework.generics import ListAPIView


class LeaderBoardViewSet(viewsets.ModelViewSet):
    queryset = LeaderBoard.objects.all()
    serializer_class = LeaderBoardSerializer


class RoundViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    queryset = Round.objects.all()
    serializers = {
        'create': CreateUpdateRoundSerializer,
        'partial_update': CreateUpdateRoundSerializer,
        'default': RoundSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        if self.action in ('update', 'create', 'delete'):
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ('retrieve',):
            self.permission_classes = [IsRoundPermitted, ]
        return super(self.__class__, self).get_permissions()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, args, kwargs)


class HintsViewSet(viewsets.ModelViewSet):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializers = {
        'create': CreateUpdateQuestionSerializer,
        'partial_update': CreateUpdateQuestionSerializer,
        'default': ListQuestionSerializer,
    }

    def get_serializer_class(self):
            return self.serializers.get(self.action, self.serializers['default'])


class DashboardViewSet(ListAPIView):
    queryset = Round.objects.all()
    serializer_class = DashboardSerializer


