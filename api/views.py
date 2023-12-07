from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.response import Response

@api_view(['GET'])
def getData(request):
    person = {'name': 'Dennis', 'age': 28}
    return Response(person)