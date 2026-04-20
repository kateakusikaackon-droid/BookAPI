from rest_framework import viewsets, status, generics 
from rest_framework.decorators import action 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny 
from django.contrib.auth.models import User 
from .models import Book 
from .serializers import BookSerializer, UserSerializer  

class RegisterView(generics.CreateAPIView):     
    queryset = User.objects.all()     
    permission_classes = [AllowAny]     
    serializer_class = UserSerializer  
    
class BookViewSet(viewsets.ModelViewSet):     
    queryset = Book.objects.all()     
    serializer_class = BookSerializer     
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):  
        serializer.save(created_by=self.request.user)

    #✅ Custom endpoint: /api/books/my_books/
    @action(detail=False, methods=['get'])   #A decocorator adds a certain attibute to a function. A decorator is a custom action and also adds a custom end point(and address). #This custom endpoint (a decorator)above is aiming at a part of the backend..and that part will be accessed by using this URL= booksbackend.com/books/my_books/      
    def my_books(self, request):         
        books = Book.objects.filter(created_by=request.user)         
        serializer = self.get_serializer(books, many=True)         
        return Response(serializer.data)   
          
    ## ✅ Custom endpoint: /api/books/search/?q=...
    @action(detail=True, methods=['get'])     
    def search(self, request):         
        query = request.query_params.get('q', '') 
        books = Book.objects.filter(title__icontains=query) | \
                Book.objects.filter(author__icontains=query)         
        serializer = self.get_serializer(books, many=True)         
        return Response(serializer.data)



#API endpoint for creating new user = booksbackend.com/books/perform_create
#API endpoint for creating filtering or getting the lists of books = booksbackend.com/books/my_books

#API endpoint if user wants to search for a book= booksbackend.com/book

#searching means querying
# q is query string identifyer
# example of a query:   .../books/search/?q=donald+trump