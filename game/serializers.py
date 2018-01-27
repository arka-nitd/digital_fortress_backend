from rest_framework import serializers
from game.models import LeaderBoard, Round, Hint, Question


class LeaderBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaderBoard
        extra_kwargs = {
            'id': {'read_only': True},
        }
        fields = ('id', 'user', 'round')


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        extra_kwargs = {
            'id': {'read_only': True},
        }
        fields = ('round', 'title', 'detail')


class CreateUpdateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        extra_kwargs = {
            'id': {'read_only': True},
            'position': {'write_only': True},
        }
        fields = ('number', 'title', 'detail', 'round', 'answer', 'position')


class ListQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        extra_kwargs = {
            'id': {'read_only': True},
        }
        fields = ('id', 'number', 'title', 'detail',)


class DashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = ('number', 'title', 'detail')


class RoundSerializer(serializers.ModelSerializer):

    question_set = ListQuestionSerializer(many=True)

    class Meta:
        model = Round
        extra_kwargs = {
            'id': {'read_only': True },
        }
        fields = ('id', 'number', 'title', 'detail', 'answer', 'question_set')


class CreateUpdateRoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        extra_kwargs = {
            'id': {'read_only': True },
        }
        fields = ('id', 'number', 'title', 'detail', 'answer', )