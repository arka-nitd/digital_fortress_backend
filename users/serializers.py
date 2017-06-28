from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model
from game.models import LeaderBoard, Round
from game.serializers import LeaderBoardSerializer

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
        }
        fields = (
            'id',
            'email',
            'username',
            'date_joined',
            'password',
            'is_superuser',
        )

    def create(self, validated_data):
        user = get_user_model()

        if validated_data.pop('is_superuser', False):
            return user.objects.create_superuser(**validated_data)
        else:
            user_instance = user.objects.create_user(**validated_data)
            first_round = Round.objects.filter(number=1).first()
            LeaderBoard.objects.create(
                user = user_instance,
                round = first_round
            )
            return user_instance

class LeaderBoardListing(serializers.RelatedField):
    obj={}
    def to_representation(self, value):
        self.obj['round_id'] = value.id
        return self.obj

class UserSerializer(serializers.ModelSerializer):

    current_round = serializers.ReadOnlyField(source='leaderboard.round.id', read_only=True)

    class Meta:
        model = User
        extra_kwargs = {
            'email': {'read_only': True},
            'id': {'read_only': True},
            'date_joined': {'read_only': True},
        }
        fields = (
            'id',
            'first_name',
            'username',
            'last_name',
            'email',
            'date_joined',
            'current_round',
        )
