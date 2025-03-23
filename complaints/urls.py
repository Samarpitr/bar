from django.urls import path

from . import views
from .models import ComplaintAndSuggestion

urlpatterns = [
path('complaints/', views.ComplaintAndSuggestionListView.as_view(), name='complaint_list'),
path('complaints/<int:pk>/', views.ComplaintAndSuggestionDetailView.as_view(), name='complaint_detail'),
path('complaints/new/', views.ComplaintAndSuggestionCreateView.as_view(), name='complaint_create'),
path('complaints/<int:pk>/edit/', views.ComplaintAndSuggestionUpdateView.as_view(), name='complaint_edit'),
path('complaints/<int:pk>/delete/', views.ComplaintAndSuggestionDeleteView.as_view(), name='complaint_delete'),
]