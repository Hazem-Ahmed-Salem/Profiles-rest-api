from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from profiles_api import views


VSF_router = DefaultRouter()
VSF_router.register('viewset-features',views.ViewSetFeatures,basename='viewset-features')

urlpatterns = [
    path('apiview-features/',views.APIViewFeatures.as_view()),
    path('',include(VSF_router.urls)),
]