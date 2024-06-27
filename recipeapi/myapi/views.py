from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.views import APIView

# Create your views here.

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


    def delete(self, request, *args, **kwargs):
        Recipe.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'


