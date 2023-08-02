from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


#Vista para Listar
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAdminUser] #Se requiere Autenticacion par el registro
    authentication_classes = []  # No se requiere autenticación para el registro

#Vista para ver el detalle del Usuario
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAdminUser] #Se requiere Autenticacion par el registro
    permission_classes = [] # No se requiere autenticación para el registro


# (Vista views) para el Login
class MyTokenObtainPairView(TokenObtainPairView):
    # Personalizar la respuesta del token de acceso
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.user
        response.data['user_id'] = user.id
        response.data['email'] = user.email
        response.data['name'] = user.name
        response.data['last_name'] = user.last_name
        response.data['is_staff'] = user.is_staff
        return response






