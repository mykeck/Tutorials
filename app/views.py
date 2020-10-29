from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Articles
from .serializers import ArticlesSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def article_list(request):

    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles,many = True)
        return  JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticlesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)  


@csrf_exempt
def article_detail(request,pk):
    try: 
        article = Articles.objects.get(pk=pk) 

    except Articles.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticlesSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400) 


    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)     

