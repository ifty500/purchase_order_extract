from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    #path('upload/', views.upload, name='upload'),
    path('pos/', views.po_list, name='po_list'),
    path('pos/upload/', views.upload_po, name='upload_po'),
    path('pos/<str:pk>/', views.delete_po, name='delete_po'),

    #path('pos/upload_size/', views.upload_size, name='upload_size'),
    #path('pos/size_list', views.size_list, name='size_list'),

    path('admin/', admin.site.urls),
    # path('po_upload_page/', views.po_upload_page, name='po_upload_page'),
    # path('po_upload/',views.po_upload, name='po_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
