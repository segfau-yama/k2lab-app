from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entry_exit_app.urls')),
    path('accounts/', include('accounts_app.urls')),
]
