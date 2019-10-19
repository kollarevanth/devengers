from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# Create your views here.
@api_view(['POST'])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Test(heightdata):
    try:
        return JsonResponse("Anil Sir",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)