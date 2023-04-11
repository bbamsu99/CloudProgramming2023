import os.path

from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True )


    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True )


    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30) # 4/11사용자에게 입력받아야함
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) # 4/11자동으로 생성
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE) # 4/11null true, 대문자 set_null 로 하면 안써도 none으로 된다
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'[{self.pk}] {self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)