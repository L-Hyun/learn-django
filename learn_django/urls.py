from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include('polls.urls')),
    path("accounts/", include('accounts.urls')),
    path("items/", include('items.urls'))
]
