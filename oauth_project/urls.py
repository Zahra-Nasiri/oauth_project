from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))

]
