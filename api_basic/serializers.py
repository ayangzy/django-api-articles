
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'email']
    # title = serializers.CharField(max_length=200)
    # author = serializers.CharField(max_length=100)
    # email = serializers.CharField(max_length=100)
    # date = serializers.DateTimeField(auto_now_add=True)


    # def create(self, validate_data):
    #     return Article.objects.create(validate_data)
    
    # def update(self, instance, validate_data):
    #     instance.title = validate_data.get('title', instance.title)
    #     instance.author = validate_data.get('author', instance.author)
    #     instance.email = validate_data.get('email', instance.email)
    #     instance.date = validate_data.get('date', instance.date)
    #     instance.save()
    #     return instance
    