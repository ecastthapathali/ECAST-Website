
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('committee.urls')),
    path('intake/', include('intake_form.urls')),
]
