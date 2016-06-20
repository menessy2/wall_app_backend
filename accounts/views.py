from accounts.models import CustomerUser
from rest_framework import viewsets
from serializers import CustomerUserSerializer, LoginSerializer, LoginResponseObject, LoginResponseSerializer, DummyResponseSerializer
from rest_framework.decorators import list_route
from permissions import UserPermission
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout


class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomerUser.objects.all()
    permission_classes = (UserPermission,)
    http_method_names = ['get', 'post', 'put', 'head']     # This line is intended for not allowing delete method

    def get_serializer_class(self):
        if self.action == 'login_user':
            return LoginSerializer
        return CustomerUserSerializer


    @list_route(methods=['post'], url_path='login')
    def login_user(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            response_obj = LoginResponseObject(is_authenticated=False)
            response_obj.set_message_invalid_input()
            serialized = LoginResponseSerializer(response_obj)
            return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)

        account = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if account is not None:
            if account.is_active:
                login(request, account)
                response_obj = LoginResponseObject(is_authenticated=True,additional_message=request.session.session_key)
                serialized = LoginResponseSerializer(response_obj)
                return Response(serialized.data)
            else:
                response_obj = LoginResponseObject(is_authenticated=False)
                response_obj.set_message_inactive_user()
                serialized = LoginResponseSerializer(response_obj)
                return Response(serialized.data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response_obj = LoginResponseObject(is_authenticated=False)
            response_obj.set_message_wrong_credentials()
            serialized = LoginResponseSerializer(response_obj)
            return Response(serialized.data, status=status.HTTP_401_UNAUTHORIZED)



    @list_route(methods=['get'], url_path='logout')
    def logout_user(self, request):
        logout(request)
        serialized = DummyResponseSerializer(object())
        return Response(serialized.data)