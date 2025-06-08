from django.urls import path, include
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet
from rest_framework_nested import routers as r

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
conversations_router = r.NestedDefaultRouter(router, r'conversations', lookup='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversations_router.urls)),
]
