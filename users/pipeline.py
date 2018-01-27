from game.models import LeaderBoard, Round

USER_FIELDS = ['username', 'email']


def create_user_and_leaderboard_entry(backend, strategy, user, details, response, *args, **kwargs):

    if user:
        return {'is_new': False}

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))
    if not fields:
        return

    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        fields.update({'avatar': url})

    user = strategy.create_user(**fields)

    LeaderBoard.objects.create(user=user, round=Round.objects.get(number=Round.BASE))

    return {
        'is_new': True,
        'user': user
    }
