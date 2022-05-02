from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getMovies(request):
    return(Response({"routeTo":"getMovies"}))

@api_view(['POST'])
def addMovie(request):
    return(Response({"routeTo":"addMovie", "POST":request.data}))

@api_view(['PUT'])
def updateMovie(request, id = None):
    return(Response({"routeTo":"updateMovie", "id":id, "PUT": request.data}))

@api_view(['DELETE'])
def deleteMovie(request, id = None):
    return(Response({"routeTo":"deleteMovie", "id":id}))
