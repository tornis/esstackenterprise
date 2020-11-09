from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main.views import (
    HomePageView, searchTerm
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r'^search/', searchTerm, name="search")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
