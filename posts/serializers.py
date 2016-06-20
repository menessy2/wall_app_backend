from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.SlugRelatedField(read_only=True, slug_field='username')
    creation_time = serializers.SerializerMethodField()

    def get_creation_time(self, obj):
        return obj.creation_time.strftime("%d/%m/%y %I:%M %p")

    class Meta:
        model = Post
        fields = ('id', 'creation_time', 'last_edit', 'creator', 'content')
        read_only_fields = ('id','creation_time','last_edit','creator')