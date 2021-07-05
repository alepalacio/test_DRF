from django.shortcuts import render
"""
VIEWS IMPORTS
from django.http import HttpResponse, JsonResponse
"""

"""
@api_view DECORATORS IMPORTS
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
"""
from rest_framework.response import Response
from rest_framework import status

"""
APIView IMPORTS
from rest_framework.views import APIView
"""

"""
GENERIC VIEWS AND MIXINS IMPORTS
"""
from rest_framework import generics
from rest_framework import mixins

""""
AUTHENTICATION
"""
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
"""
GENERIC VIEWS AND MIXINS
"""

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = Article.objects.all()

    lookup_field = 'id'

    def get_serializer_class(self):
        return ArticleSerializer

    #Basic authentications
    #authentication_classes = [SessionAuthentication, BasicAuthentication]

    #Token authentication
    authentication_classes = [TokenAuthentication]

    permission_class = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


"""
CLASS BASED VIEWS
"""
# class ArticleAPIView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SingleArticleAPIView(APIView):
    
#     #Getting data from a single element to work with it on differents views

#     def get_article(self, pk):
#         try:
#             return Article.objects.get(id=pk)
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_BAD_REQUEST)

#     def get(self, request, pk):
#         article = self.get_article(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         article = self.get_article(pk)
#         serializer = ArticleSerializer(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         article = self.get_article(pk)
#         article.delete()
#         return Response('Article successfully deleted')

"""
@API_VIEW DECORATOR FOR FUNCTION BASED VIEWS
"""
# @api_view(['GET', 'POST'])
# def article_list (request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_single (request, pk):
#     try:
#         article = Article.objects.get(id=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response('Article successfully deleted')

"""
VIEWS
"""

# @csrf_exempt
# def article_list (request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_single (request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)