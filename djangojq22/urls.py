from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,re_path
from .views import CreateCategory,UpdateCategory,show_category,CreateStudent,CreateCategory2,CategoryList
app_name='djangojq22'
urlpatterns=[
    path('', views.index, name='index'),
    re_path('index/', views.index, name='main-index'),
    re_path('CreateCategory/', CreateCategory.as_view(), name='CreateCategory'),
    re_path('CreateCategory2/', CreateCategory2.as_view(), name='CreateCategory2'),
    re_path('CategoryList/', CategoryList.as_view(), name='CategoryList'),

    re_path('UpdateCategory/(?P<pk>[0-9]+)/', UpdateCategory.as_view(), name='UpdateCategory'),
    re_path('show_category/(?P<category_pk>[0-9]+)/', views.show_category, name='show_category'),
    re_path(r'^category_like/$', views.like_category, name='like_category'),

    re_path(r'^listing/$', views.listing, name='listing'),
    re_path('CreateStudent/', CreateStudent.as_view(), name='CreateStudent'),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for upload of profile pic
