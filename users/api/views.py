from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    user = UserSerializer(request.user)
    return Response(user.data)

@api_view(['POST'])
def addUser(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid() and serializer.validate(attrs=request.data):
            serializer.create(validated_data=request.data)
            return Response({'register':'user created successfully','user':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
