from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cat
from .serializes import CatSerializer

@login_required
@api_view(['GET'])
def getCatData(request):
    user = request.user
    cats = Cat.objects.filter(user=user)
    count = cats.count()
    serializer = CatSerializer(cats, many=True)
    print(cats)
    return Response({"count":count})
