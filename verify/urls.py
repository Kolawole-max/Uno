from django.urls import path
from verify import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.SaveImageFace, name="index")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)