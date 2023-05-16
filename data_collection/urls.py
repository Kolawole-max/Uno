from django.urls import path
from data_collection import views
from django.conf.urls.static import static
from django.conf import settings
#from company import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile ,name="profile"),

    #Registration
    path("personal/", views.create_data, name="create_data"),
    path("address/", views.address_data ,name="address_data"),
    path("documents/", views.documents_, name="documents_"),
    path("", views.verify_, name="verify"),
    
    ## API ##
    path("profile/savecode/", views.save_code, name="save_code"),
    path('image/documents_api/', views.documents_api, name='documents_api'),
    
    
    
    #path("company/login", views.company_login_view, name="adlogin"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)