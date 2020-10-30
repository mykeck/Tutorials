from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Articles
from .serializers import ArticlesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated




# Create your views here.





@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles,many = True)
        return  Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request,pk):
    try: 
        article = Articles.objects.get(pk=pk) 

    except Articles.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = ArticlesSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST) 


    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     

