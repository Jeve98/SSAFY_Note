from django.db import models

# Create your models here.
class Article(models.Model):
    # DB column(field) 생성 및 데이터 유형과 제약 조건 정의
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
-----------------------------------
ID(Django 생성) | Title | content  |
-----------------------------------
               |        |          |
-----------------------------------
"""
