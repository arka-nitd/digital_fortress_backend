from rest_framework import permissions
from game.models import Round, LeaderBoard

class IsRoundPermitted(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_staff:
            return True

        requested_round_number = Round.objects.filter(
            id=view.kwargs['pk']
        ).first().number

        current_round_number = LeaderBoard.objects.filter(
            user__id=request.user.id
        ).first().round.number

        if requested_round_number>current_round_number:
            return False
        return True