from django.urls import path
from .views import DashboardListView, AssignmentDetailView, SubmissionUpdateView, SubmissionCreateView

urlpatterns = [
    path('', DashboardListView.as_view(), name='dashboard'),
    path('assignments/<int:pk>', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignments/<int:pk>/submission', SubmissionCreateView.as_view(), name='submit-assignment')
]