from accounts.views import UserViewSet
from posts.views import PostViewSet
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'accounts', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]