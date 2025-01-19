from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('viewset-features',views.ViewSetFeatures,basename='viewset-features')

"""we didn't specify a basename like in the features of viewsets because this view set has a queryset so django configures the name with the name of the model."""
router.register('profile',views.UserProfileViewSet)


urlpatterns = [
    path('apiview-features/',views.APIViewFeatures.as_view()),
    path('',include(router.urls)),
]