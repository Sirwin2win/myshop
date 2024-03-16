from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
 # post views
 path('', views.product_list, name='product_list'),
 path('prod_list', views.prod_list, name='prod_list'),
#  path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
 path('create_product/', views.create_product, name='create_product'),
 path('create_category/', views.create_category, name='create_category'),
 path('update_category/<int:id>/', views.update_category, name='update_category'),
 path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
 path('update_product/<int:id>/', views.update_product, name='update_product'),
 path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
 path('category/', views.category_list, name='category_list'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
 path('portal/', views.portal, name='portal'),
 path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
 path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)