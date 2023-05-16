from django.urls import path, reverse_lazy
from django.contrib.auth import logout
from company import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("login/", views.company_login_view, name="adlogin"),
    path('register/', views.company_register_view, name="adreg"),
    path('', views.company_dashboard, name="admin_dashboard"),
    path('logout/', views.company_logout_view, name="company_logout"),
    path('search/', views.search_user, name="search_user"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)