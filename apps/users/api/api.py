from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from django_rest_blog.apps.users.models import User
from rest_framework.decorators import api_view, authentication_classes

from apps.users.api.serializers import UserSerializer, UserListSerializer, UserSerializers
from apps.users.models import User
# from django_rest_blog.apps.users.api.serializers import UserSerializer, UserListSerializer

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)


@api_view(['GET', 'POST'])
def user_api_view(request):
    # permission_classes = (IsAuthenticated,)
    # list
    if request.user.is_authenticated:

        if request.method == 'GET':
            # queryset
            users = User.objects.all().values('id', 'username', 'email', 'password', 'name')
            users_serializer = UserListSerializer(users, many=True)

            # test_data = {
            #     'name':'developer',
            #     'email':'a@gmail.com'
            # }
            # test_users = TestUserSerializer(data = test_data, context = test_data)
            # if test_users.is_valid():
            #     user_instance =test_users.save()
            #     print(user_instance)
            #     # print("paso validaciones")
            # else:
            #     print(test_users.errors)

            return Response(users_serializer.data, status=status.HTTP_200_OK)
        # create
        elif request.method == 'POST':
            users_serializer = UserSerializer(data=request.data)
            # validation
            if users_serializer.is_valid():
                users_serializer.save()
                # return Response({'message': 'Usuario Eliminado correctamente!!'}, status=status.HTTP_201_CREATED)
                return Response(users_serializer.data, status=status.HTTP_201_CREATED)

            return Response(users_serializer.errors)
    else:
        return Response({'message': 'Inicie Sesion!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes((TokenAuthentication,))
def user_detail_api_view(request, pk=None):
    # consulta
    user = User.objects.filter(id=pk).first()
    if request.user.is_authenticated:
        # validacion
        if user:
            # retrieve
            if request.method == 'GET':

                users_serializer = UserSerializer(user)
                return Response(users_serializer.data, status=status.HTTP_200_OK)
            # update
            elif request.method == 'PUT':

                users_serializer = UserSerializer(user, data=request.data)
                # users_serializer = UserSerializer(user, data=request.data)
                if users_serializer.is_valid():
                    users_serializer.save()
                    return Response(users_serializer.data, status=status.HTTP_200_OK)
                return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # delete
            elif request.method == 'DELETE':
                user.delete()
                return Response({'message': 'Usuario Eliminado correctamente!!'}, status=status.HTTP_200_OK)

        return Response({'message': 'No se ha encontrado un usuario con estos datos'},
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Inicie Sesion!!'}, status=status.HTTP_400_BAD_REQUEST)


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('usuario_api1')

    @method_decorator(csrf_exempt)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            # return Response({'message': 'Inicie Sesion!!'}, status=status.HTTP_200_OK)

            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'message': 'Cerro Sesion!!'}, status=status.HTTP_200_OK)


from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializers(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        token_cr = ''
        post = ''
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # if (request.user.is_authenticated):
        # if user:

        # if not (request.user.is_superuser):
        # if user:
        # if user.is_authenticated:

        if user:
            login(request, user)
            tk = AuthToken.objects.filter(user_id=request.user.id).first()

            if tk is None:
                token_cr = AuthToken.objects.create(user)[1]
                post = AuthToken.objects.filter(user_id=request.user.id).first()
            else:
                token_cr = tk.digest
                post = tk
            if post.user.image != '':
                photo_url = post.user.image.url
                image = request.build_absolute_uri(photo_url)
            else:
                image = 'http://127.0.0.1:8000/static/img/empty.png'

            return Response({
                'id': post.user.id,
                'username': post.user.username,
                'name': post.user.name,
                'email': post.user.email,
                'password': post.user.password,
                'image': image,
                'token': token_cr
            })

        # else:
        #     login(request, user)
        #     # if (request.user.is_superuser):
        #     tks = AuthToken.objects.filter(user_id=request.user.id).first()
        #     if tks is None:
        #         token_cr = AuthToken.objects.create(user)[1]
        #         post = AuthToken.objects.filter(user_id=request.user.id).first()
        #     else:
        #         token_cr = tks.digest
        #         post = tks.user.id
        #     print("2")
        #     # if (request.user.id == tks.user.id):
        #     return Response({
        #         'id': post,
        #         'username': user.username,
        #         'name': user.name,
        #         'email': user.email,
        #         'password': user.password,
        #         'token': token_cr
        #     })
        #

        # tks = AuthToken.objects.create(user)[1]
        # print(tks)
        # token = AuthToken.objects.get(user_id=request.user.id)
        # print(token)
        # return Response({
        #     # "user": UserSerializers(LoginAPI, context=self.post(request)),
        #     "token": AuthToken.objects.create(user)[1]
        # })
        # return super(LoginAPI, self).post(request)
