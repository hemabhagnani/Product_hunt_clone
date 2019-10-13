
from django.contrib import admin
from django.urls import path
from django.urls import include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name='home'),
    path('accounts/', include('accounts.urls')),
]
