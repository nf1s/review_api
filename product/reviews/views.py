import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from markdown import markdown

from reviews.forms import ReviewForm
from reviews.models import Review


class AssignmentView(TemplateView):
    template_name = 'reviews/assignment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(os.path.join(os.path.dirname(settings.BASE_DIR), 'README.md'), encoding='utf-8') as f:
            assignment_content = f.read()

        context.update({
            'assignment_content': mark_safe(markdown(assignment_content))
        })

        return context


class DashboardView(LoginRequiredMixin, ListView):
    model = Review
    ordering = ('-start_date',)
    context_object_name = 'reviews'
    template_name = 'reviews/dashboard.html'

    def get_queryset(self):
        reviews = super().get_queryset()
        reviews = reviews.select_related('company')

        return reviews


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('dashboard')
