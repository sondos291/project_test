
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomeUser
from .serializer import UserSerializer,TokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairSerializer

class UserSignUpView(generics.CreateAPIView):
    queryset = CustomeUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if the username or email already exists
            if CustomeUser.objects.filter(username=request.data.get('username')).exists():
                return Response({'detail': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if CustomeUser.objects.filter(email=request.data.get('email')).exists():
                return Response({'detail': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the user if everything is valid
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({
                'user': {
                    'username': user.username,
                    'email': user.email,
                },
                'tokens': tokens,
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        
        # If the serializer is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(generics.GenericAPIView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        user = CustomeUser.objects.filter(username=request.data.get('username')).first()
        if user and user.check_password(request.data.get('password')):
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({
                'tokens': tokens,
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

















































