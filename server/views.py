from rest_framework.decorators import api_view # aqui importamos api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from server.serializers import UserSerializer # importamos el serializador de usuario
from django.shortcuts import get_object_or_404


from rest_framework.decorators import authentication_classes, permission_classes # sirve para agregar autenticacion y permisos
from rest_framework.authentication import TokenAuthentication # importamos la autenticacion por token
from rest_framework.permissions import IsAuthenticated # importamos el permiso para usuarios autenticados


@api_view(['GET'])  # Decorador para especificar que esta vista maneja solicitudes GET
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['POST'])  # Decorador para especificar que esta vista maneja solicitudes POST
def login(request):
    user = get_object_or_404(User, username=request.data.get('username')) # obtenemos el usuario por su nombre de usuario
    if not user.check_password(request.data.get('password')): # aqui verificamos la contraseña
       return Response({"error": "Invalid credentials"}, status=400) # devolvemos error si la contraseña es incorrecta
    
    token = Token.objects.get_or_create(user=user) # obtenemos o creamos un token para el usuario
    UserSerializer(instance=user) # serializamos el usuario
    return Response({"message": "Login successful", "token": token[0].key}) # devolvemos el token

@api_view(['POST'])  
def register(request):
    serializer = UserSerializer(data=request.data) # usamos el serializador de usuario
    if serializer.is_valid(): # verificamos si los datos son validos
        serializer.save() # guardamos el nuevo usuario

        user = User.objects.get(username=serializer.data['username']) # obtenemos el usuario creado
        user.set_password(serializer.data['password']) # ciframos la contraseña
        user.save() # guardamos el usuario con la contraseña cifrada

        token = Token.objects.create(user=user) # creamos un token para el usuario
        return Response({"message": "Registration successful", "token": token.key}) # devolvemos el token
    
    return Response(serializer.errors, status=400) # devolvemos errores si los hay



@api_view(['POST'])  
@authentication_classes([TokenAuthentication])  # especificamos la autenticacion por token
@permission_classes([IsAuthenticated])  # especificamos que el usuario debe estar autenticado
def profile(request):
    user = request.user  # obtenemos el usuario autenticado
    return Response({ " Estas logueado con los datos del usuario": user.username})  # devolvemos el perfil del usuario

   