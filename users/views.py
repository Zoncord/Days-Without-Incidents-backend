from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.permissions import IsCurrentUserOrReadOnly
from users.serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsCurrentUserOrReadOnly]


class ProfileView(APIView):
    """Returns information about the current user"""

    def get(self, request):
        user = User.objects.get(id=2)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class AuthorizationView(APIView):
    """"""

    def post(self, request):
        if 'code' not in request.POST:
            return Response({'error': 'invalid code'}, status=400)
        client_id = 'Art6vlzoqZKTolSIwqhO3vjlx01zung3OkT4ZXpH'
        client_secret = 'BhuIALWmd7mQGN4DIF6C7Kr2cRRAkB5yGQJB7uLGqGnAnwnzu6t4WLGn4l689TTLxGbM0M9Em9i1pzSgfy5aPIhkoOSsa4aQH0WQl7HgZyGBNxRQbL7tEAG6s8PNE1p8'

        authorization_token = Token.objects.get_or_create(user_id=1)[0]
        return Response({'authtoken': authorization_token})
