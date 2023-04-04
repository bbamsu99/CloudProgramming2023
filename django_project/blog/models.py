from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
    #시발왜안되누
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
    #override 한 것이다

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    #누가 썼는지는 유저와 연동필요