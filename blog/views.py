from django.db.models import Count
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.filters import PostFilter
from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.annotate(likes_count=Count('ratings__id')).order_by('-likes_count')
    serializer_class = PostSerializer

    permission_classes = [IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'date_time_of_creation', 'ratings']
    search_fields = ['title']
    filterset_class = PostFilter
