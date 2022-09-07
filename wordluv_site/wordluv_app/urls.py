from django.urls import path
from . import views

urlpatterns = [
    path('', views.WordListView, name='wordslist'),
#    path('<word_id>/', views.WordDetail, name='worddetail')
    path('<int:pk>/', views.WordDetailViewId.as_view(), name='worddetailId'),
    path('<slug:slug>/', views.WordDetailViewSlug.as_view(), name='worddetailSlug'),
]