from django.urls import path
from . import views

urlpatterns = [
    path('', views.WordListView, name='wordslist'),
    path('add_new/', views.WordCreateView.as_view(), name='wordCreate'),
#    path('<word_id>/', views.WordDetail, name='worddetail')
    path('<int:pk>/', views.WordDetailViewId.as_view(), name='worddetailId'),
    path('<slug:slug>/', views.WordDetailViewSlug.as_view(), name='worddetailSlug'),
    path('<slug:slug>/update/', views.WordUpdateView.as_view(), name='wordUpdate'),
    path('<slug:slug>/delete/', views.WordDeleteView.as_view(), name='wordDelete'),

]