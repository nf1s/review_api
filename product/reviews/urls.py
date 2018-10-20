from django.conf.urls import url

from reviews.views import AssignmentView, DashboardView, ProjectUpdateView


urlpatterns = [
    url(r'^$', AssignmentView.as_view(), name='assignment'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^reviews/(?P<pk>[0-9]+)-(?P<slug>[-\w]*)/$', ProjectUpdateView.as_view(), name='project-update'),
]
