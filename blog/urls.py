from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>', views.detail, name='detail'),
]
