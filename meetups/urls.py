from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/meetups')),
    path('meetups/', include('mymeetups.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
