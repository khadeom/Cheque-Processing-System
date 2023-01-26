from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# how to import include in django?



urlpatterns = [
    path("",views.Home.as_view()),

    path("accounts/", include("django.contrib.auth.urls")), 

    path('home/', views.home ,name='home' ),
    path('home/upload/',views.upload_cheque,name="cheque_upload"),
    path('home/upload2/',views.upload_cheque2,name="cheque_upload2"),
    path('home/upload3/',views.upload_cheque3,name="cheque_upload3"),
    path('home/chequeProcessing/',views.chequeProcessing,name="chequeProcessing"),
    path('home/viewimage/',views.viewCheque,name="viewCheque"),
    path('home/done',views.done,name="done"),   
    path('home/viewall',views.viewAll, name="viewAll"), 






]+static("/media/", document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
