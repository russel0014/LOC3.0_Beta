from django.contrib import admin
from django.urls import path ,include
from django.conf import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("job.urls") ),
]
