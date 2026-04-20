from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Book  

class UserSerializer(serializers.ModelSerializer):     
    password = serializers.CharField(write_only=True)    

    class Meta:         
        model = User         
        fields = ['id', 'username', 'email', 'password']          
        
    def create(self, validated_data):         
        user = User.objects.create_user( 
            username=validated_data['username'],             
            email=validated_data.get('email', ''),             
            password=validated_data['password']         
        )         
        return user 
    
class BookSerializer(serializers.ModelSerializer):     
        created_by_username = serializers.CharField(source='created_by.username', read_only=True) 

        class Meta:         
            model = Book         
            fields = [
                'id', 'title', 'author', 'isbn', 'published_date',                    
                'pages', 'description', 'created_by', 'created_by_username',                   
                'created_at', 'updated_at'
                ]         
            read_only_fields = ['created_by', 'created_at', 'updated_at']



