from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TblTest

class UserLogin(APIView):
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'message': 'Error : Please provide both username and password'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Authenticate user
        user = TblTest.objects.filter(username_tmu=username, password_tmu=password).first()
        if user is not None:
            return Response({'message': 'Sussess : Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error : Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
