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

    # New
    path('course-get-create', CourseView.as_view()),
    path('course-delete-update', DeleteUpdateCourseView.as_view()),

    path('stuff-get-create', StuffView.as_view()),
    path('stuff-delete-update', DeleteUpdateStuffView.as_view()),

    path('admin-get-create', AdministrationView.as_view()),
    path('admin-delete-update', DeleteUpdateAdministrationView.as_view()),

    path('masters-cost-get-create', MastersCostTableView.as_view()),
    path('masters-cost-delete-update', DeleteUpdateMastersCostTableView.as_view()),

    path('phd-cost-get-create', PhdCostTableView.as_view()),
    path('phd-cost-delete-update', DeleteUpdatePhdCostTableView.as_view()),

    path('important-information-get-create', ImportantInformationView.as_view()),
    path('important-information-delete-update', DeleteUpdateImportantInformationView.as_view()),

    path('gallery-get-create', GalleryView.as_view()),
    path('gallery-delete-update', DeleteUpdateGalleryView.as_view()),

]
