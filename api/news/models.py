from django.db import models


# Create your models here.
class News(models.Model):
    title = models.TextField()
    img = models.TextField()
    article = models.TextField(default='Default Article Text')
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
