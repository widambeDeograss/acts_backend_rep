from django.urls import path
from .views import *

app_name = 'siteManager'

urlpatterns = [
    path('contact', ContactView.as_view()),
    path('application', ApplicationView.as_view()),
    path('event', EventView.as_view()),
    path('event-actions/<slug:event_id>', EventActions.as_view()),
    path('single-event/<slug:event_id>', SingleEvent.as_view()),
    path('delete-contact/<slug:contact_id>', DeleteContact.as_view()),
    path('dashboard', DashboardView.as_view()),

]
