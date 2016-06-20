from posts.models import Post
from rest_framework import viewsets
from rest_framework.decorators import list_route
from permissions import PostPermission
from rest_framework.response import Response
from posts.serializers import PostSerializer



class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = (PostPermission,)
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'head']     # This line is intended for not allowing delete method


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # It was overrided specifically for reversing the order of the posts, by default
    def list(self, request):
        queryset = self.queryset.order_by('-creation_time')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)