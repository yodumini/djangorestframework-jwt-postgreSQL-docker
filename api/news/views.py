# Create your views here.
from news.models import News
from news.serializers import NewsSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)