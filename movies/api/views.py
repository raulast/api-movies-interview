from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from movies.models import Movie
from .serializers import MovieSerializer,AddMovieSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOwnsMovies(request):
    user = request.user
    ownMovies = user.movie_set.all()
    if len(ownMovies) > 0:
        return(Response({"ownMovies":"ownMovies"}))
    return(Response(ownMovies))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMovie(request):
    user = request.user
    serializer = AddMovieSerializer(data=request.data)
    if serializer.is_valid() and serializer.validate(attrs=request.data):
        request.data['owner']=user
        serializer.create(validated_data=request.data)
        return Response({'register':'Movie created successfully','movie':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMovie(request, id = None):
    user = request.user
    return(Response({"routeTo":"updateMovie", "id":id, "PUT": request.data}))

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMovie(request, id = None):
    user = request.user
    return(Response({"routeTo":"deleteMovie", "id":id}))
