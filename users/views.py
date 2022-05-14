from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.permissions import IsCurrentUserOrReadOnly
from users.serializers import UserSerializer, ProfileSerializer
from users.services import update_user_token
from users.errors import IncorrectCode, CodeNotProvided


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsCurrentUserOrReadOnly]


class ProfileView(APIView):
    """Returns information about the current user"""

    def get(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated()
        user = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class AuthorizationView(APIView):
    """"""

    def post(self, request):
        print(request.data['code'])
        return Response({'token': str(Token.objects.get_or_create(user_id=2)[0])})
        try:
            token = update_user_token(request)
        except IncorrectCode:
            return Response({'error': 'Wrong security code'}, status=400)
        except CodeNotProvided:
            return Response({'error': 'Access code was not provided'}, status=400)

        return Response({'token': token})
