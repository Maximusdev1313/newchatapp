from django.urls import path, include
from .views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('api', MassageViewSet)
router.register('comment', CommentViewSet)
router.register('simple', SimpleFilesViewSet)
router.register('files', FileViewSet)

urlpatterns = [
    path('', include(router.urls) ),
    # path('/simple/', include(router.urls) )
]