from cgitb import lookup
from gc import get_objects
from pickle import NONE
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class GenericAPIView(generics.GenericAPIView, 
                     mixins.ListModelMixin, 
                     mixins.CreateModelMixin, 
                     mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin
                     ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    lookup_field = 'id'
    
    def get(self, request, id=NONE):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

    def put(self, request, id=NONE):
        return self.update(request, id)
    
    def delete(self, request, id = NONE):
        return self.destroy(request, id)



        
   
