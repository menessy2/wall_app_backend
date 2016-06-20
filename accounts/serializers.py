from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from wall_app.settings import EMAIL_HOST_USER


class CustomerUserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        send_mail(
            'Registration Welcome Message !!',
            'Welcome User.',
            EMAIL_HOST_USER,
            [validated_data['email']],
            fail_silently=False,
        )
        return user


    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(allow_blank=False,allow_null=False)
    password = serializers.CharField(allow_blank=False,allow_null=False)


class LoginResponseObject(object):
    def __init__(self, is_authenticated, additional_message=''):
        self.is_authenticated = is_authenticated
        self.message = additional_message

    def set_message_inactive_user(self):
        self.message = 'Sorry, User is not active.'

    def set_message_wrong_credentials(self):
        self.message = 'Username/password combination invalid.'

    def set_message_invalid_input(self):
        self.message = 'Invalid input entered.'


class LoginResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    is_authenticated = serializers.BooleanField()


class DummyResponseSerializer(serializers.Serializer):
    pass