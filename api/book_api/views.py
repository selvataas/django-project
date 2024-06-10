from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework import status # type: ignore

@api_view(['GET', 'POST'])
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
         serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT','DELETE'])
def book(request, id):
    try:
        book = Book.objects.get(pk=id)
    except:
        return Response({"error": "Eşleşen bir kayıt bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == "GET":
          serializer = BookSerializer(book, data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
          return Response(serializer.errors)

    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)