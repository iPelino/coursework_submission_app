from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Assignment, Submission
import pytz
from datetime import datetime, timedelta


class DashboardListView(ListView):
    model = Assignment
    template_name = "dashboard/dashboard.html"


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'dashboard/assignment_detail.html'


class SubmissionCreateView(CreateView):
    model = Submission
    template_name = "dashboard/submission.html"
    fields = ['assignment_file', 'assignment_link', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        assign = Assignment.objects.get(id=self.kwargs['pk'])
        form.instance.assignment = assign
        return super(SubmissionCreateView, self).form_valid(form)

    @property
    def is_past_due(self):
        date = Assignment.objects.get(id=self.kwargs['pk'])
        now = pytz.utc.localize(datetime.utcnow().now()) - timedelta(hours=2)
        return now > date.due_date

    def get_context_data(self, **kwargs):
        context = super(SubmissionCreateView, self).get_context_data(**kwargs)
        context['deadline_passed'] = self.is_past_due
        return context


class SubmissionUpdateView(UpdateView):
    model = Submission
    template_name = "dashboard/submission.html"
    fields = ['user', 'assignment', 'assignment_file', 'assignment_url', 'description']

