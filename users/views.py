from rest_framework import viewsets
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
    def get(self, request):
        user = User.objects.get(id=2)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
