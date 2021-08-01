from django.urls import path
from .views import leads_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailtView, LeadCreateView, LeadUpdateView, LeadDeleteView

urlpatterns = [
    path('',LeadListView.as_view(), name="lead-list"),
    path('create/',LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/',LeadDetailtView.as_view() , name="lead-detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(), name="lead-delete"),

]
