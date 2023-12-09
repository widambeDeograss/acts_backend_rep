from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer, ChangePasswordSerializer
from django.contrib.auth import authenticate, login
from .models import User
from rest_framework.generics import UpdateAPIView
from .serializer import *


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        print(request.data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            username = data['username']
            user = User.objects.filter(username=username)
            if user:
                message = {'status': False, 'message': 'Username already exists'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()

            message = {'save': True}
            return Response(message)

        message = {'save': False, 'errors': serializer.errors}
        return Response(message)


# {
# "first_name":"Michael",
# "last_name":"Michael",
# "username":"mike",
# "email": "mike@gmail.com",
# "password": "123",
# }
class LoginView(APIView):

    @staticmethod
    def post(request):
        username = request.data.get('username')
        password = request.data.get('password')
        print('Data: ', username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(token.key)
            user_id = User.objects.get(username=username)
            user_info = UserSerializer(instance=user_id, many=False).data
            response = {
                'token': token.key,
                'user': user_info
            }

            return Response(response)
        else:
            response = {
                'msg': 'Invalid username or password',
            }

            return Response(response)

# {
#     "username": "mike",
#     "password": "123"
# }


class UserInformation(APIView):

    @staticmethod
    def get(request, query_type):
        if query_type == 'single':
            try:
                user_id = request.GET.get('user_id')
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({'message': 'User Does Not Exist'})
            return Response(UserSerializer(instance=user, many=False).data)

        elif query_type == 'all':
            queryset = User.objects.all()
            return Response(UserSerializer(instance=queryset, many=True).data)

        else:
            return Response({'message': 'Wrong Request!'})


def statusName(name):
    if name == 0:
        return 'User deleted'
    elif name == 1:
        return 'User disabled'
    elif name == 2:
        return 'User inactive'
    elif name == 3:
        return 'Default status'
    elif name == 4:
        return 'User Active'
    else:
        return 'Invalid Status'


class ChangeStatus(APIView):

    @staticmethod
    def get(request, user_id, status_to):
        try:
            status_name = statusName(status_to)
            if status_name == 'Invalid Status':
                return Response({'message': status_name})

            user = User.objects.get(id=user_id)
            user.status = status_to
            user.save()
            return Response({'message': 'Status changed to ' + status_name})

        except User.DoesNotExist:
            return Response({'message': 'User Does Not Exist'})


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': True,
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        username = request.data['username']
        email = request.data['email']
        if request.user.username == username:
            try:
                query = User.objects.get(username=username)
                query.email = email,
                query.username = username
                query.first_name = first_name
                query.last_name = last_name
                query.save()
                return Response({'message': 'success'})
            except User.DoesNotExist:
                return Response({'message': 'You can not change the email'})

        else:

            return Response({'message': 'Not Authorized to Update This User'})





