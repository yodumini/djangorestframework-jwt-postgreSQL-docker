from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ('id', 'title', 'img', 'article', 'created', 'last_modify_date')