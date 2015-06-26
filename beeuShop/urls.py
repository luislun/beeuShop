from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet
from products.views import *
from beeuShop.views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product' ),
    
    # url(r'^product/', 'products.views.product', name='product'),
    url(r'^products/$', ProductList.as_view()),
)
