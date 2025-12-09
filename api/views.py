'''API views'''

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def health_check(_request):
    '''Health check endpoint'''
    return Response({"status": "ok"})
