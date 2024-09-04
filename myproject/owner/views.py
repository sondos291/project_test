from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Owner
from adminn.models import Adminn
from  owner.serializers import Ownerserializer
from rest_framework.views import APIView

# Create your views here.
from rest_framework import viewsets

class OwnerCreateView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = Ownerserializer

    def post(self, request, *args, **kwargs):
        adminn_fk = request.data.get('adminn_fk')
        
        # Check if the provided adminn_fk is indeed an admin
        try:
            adminn = Adminn.objects.get(id=adminn_fk)
        except Adminn.DoesNotExist:
            return Response({'detail': 'Provided admin ID does not exist or is not an admin.'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Proceed with creating the owner
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            owner = serializer.save()
            return Response({
                'user': {
                    'username': owner.username,
                    'email': owner.email,
                },
                'message': 'Owner created successfully'
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



    
    
    # def updateowner(self, request, *args, **kwargs):
    #         owner_id = kwargs.get('pk')  # Get the owner ID from the URL
    #         try:
    #             owner = Owner.objects.get(id=owner_id)
    #         except Owner.DoesNotExist:
    #             return Response({'detail': 'Owner not found.'}, status=status.HTTP_404_NOT_FOUND)

    #         serializer = Ownerserializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.update_password(owner, serializer.validated_data)
    #             return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
            
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ownerUpdateView(APIView):
#     def put(self,request,pk):
#         owner=self.get_object(pk)


