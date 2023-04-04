
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),

    #path('', views.index),

    #path('<int:pk>/', views.single_post_page),
    #원래이거
    #path('<int:post_num>', views.single_post_page),
]