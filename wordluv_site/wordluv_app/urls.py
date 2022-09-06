from django.urls import path
from . import views

urlpatterns = [
    path('', views.WordListView, name='wordslist'),
    path('<word_id>/', views.WordDetail, name='worddetail')
]