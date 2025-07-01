
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('agent/', include('content_agent.urls')),
    path('writer/', include('content_writer_agent.urls')),
]
