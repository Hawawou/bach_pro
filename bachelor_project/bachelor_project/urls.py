
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

# from bachelor_project import cyber_senti

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cyber_senti.urls')),
    path('accounts/', include('allauth.urls'))
]

urlpatterns += staticfiles_urlpatterns()