from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.permissions import IsCurrentUserOrReadOnly
from users.serializers import UserSerializer
from users.services import update_user_token, get_profile_context
from users.errors import IncorrectCode, CodeNotProvided


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsCurrentUserOrReadOnly]

    http_method_names = ['get', 'put', 'delete', 'option']


class ProfileView(APIView):
    """Returns information about the current user"""

    def get(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated()
        context = get_profile_context(request)
        return Response(context)


class AuthorizationView(APIView):
    """Accepts an access code and returns an access token"""

    def post(self, request):
        try:
            token = update_user_token(request)
        except IncorrectCode:
            return Response({'error': 'Wrong security code'}, status=400)
        except CodeNotProvided:
            return Response({'error': 'Access code was not provided'}, status=400)

        return Response({'token': token})
