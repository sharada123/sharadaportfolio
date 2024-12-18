from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
  
    path('',views.home),
    path('contact',views.contact),
    # path('service',views.service),
    # path('project',views.project),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)