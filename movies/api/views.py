from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from movies.models import Movie
from .serializers import MovieSerializer, AddMovieSerializer
from django.core.paginator import Paginator


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllMovies(request):
    movies = Movie.objects.filter(public=True)
    paginator = Paginator(MovieSerializer(
        movies, many=True).data, request.GET.get('per_page', 10))
    numPage = int(request.GET.get('page', 1))
    page = paginator.page(numPage)
    lastPage = paginator.num_pages
    return Response({
        "preview": request.build_absolute_uri('/api/movies/own/?page=%s' % (numPage-1))if 1 < numPage <= lastPage else None,
        "next": request.build_absolute_uri('/api/movies/own/?page=%s' % (numPage+1))if numPage < lastPage else None,
        "total": paginator.count,
        "page_len": len(page.object_list),
        "movies": page.object_list
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOwnMovies(request):
    user = request.user
    movies = user.movie_set.all()
    paginator = Paginator(MovieSerializer(
        movies, many=True).data, request.GET.get('per_page', 10))
    numPage = int(request.GET.get('page', 1))
    page = paginator.page(numPage)
    lastPage = paginator.num_pages
    return Response({
        "preview": request.build_absolute_uri('/api/movies/own/?page=%s' % (numPage-1))if 1 < numPage <= lastPage else None,
        "next": request.build_absolute_uri('/api/movies/own/?page=%s' % (numPage+1))if numPage < lastPage else None,
        "total": paginator.count,
        "page_len": len(page.object_list),
        "movies": page.object_list
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMovie(request):
    user = request.user
    if request.method == 'POST':
        serializer = AddMovieSerializer(data=request.data)
        if serializer.is_valid() and serializer.validate(attrs=request.data):
            request.data['owner'] = user
            serializer.create(validated_data=request.data)
            return Response({'message': 'Movie created successfully', 'movie': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMovie(request, id=None):
    user = request.user
    if request.method == 'PUT':
        try:
            movie = user.movie_set.get(id=id)
        except:
            return Response({"message": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = AddMovieSerializer(data=request.data)
        if serializer.is_valid() and serializer.validate(attrs=request.data):
            request.data['owner'] = user
            serializer.update(movie, validated_data=request.data)
            return Response({'message': 'Movie updated successfully', 'movie': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMovie(request, id=None):
    user = request.user
    if request.method == 'DELETE':
        try:
            movie = user.movie_set.get(id=id)
        except:
            return Response({"message": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_200_OK)
