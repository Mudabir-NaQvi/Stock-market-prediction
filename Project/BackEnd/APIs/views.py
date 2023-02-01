from rest_framework.views import APIView
from . import Serializers
from django.http import JsonResponse
# Create your views here.

class LongTermViewSet(APIView):
    def get(self, request):
        serializer = Serializers.LongTermSerializer(
            request.data, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    


class ShortTermViewSet(APIView):
    def get(self, request):
        serializer = Serializers.ShortTermSerializer(
            request.data, context={'request': request})
        return JsonResponse(serializer.data, safe=False)