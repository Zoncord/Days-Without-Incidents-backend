from rest_framework import viewsets

from blog.filters import PostFilter
from blog.models import Post
from blog.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = []

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'date_time_of_creation']
    search_fields = ['title']
    filterset_class = PostFilter

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Post.objects.filter(Q(is_private=False) | Q(owners=self.request.user))
    #
    #     return Achievement.objects.filter(is_private=False)