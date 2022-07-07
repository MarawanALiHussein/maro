from django.urls import include, path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]