from django.urls import path

from .views import main_views

app_name = 'main_pages'

urlpatterns = [
   # main_views.py
    path('', main_views, name='main'),
    #path('<int:question_id>/', base_views.detail, name='detail'),
    #path('', main_views.index, name='index'),
    #path('recent_list/', main_views.recent_list, name='recent_list'),
]