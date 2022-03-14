from rest_framework import routers
from api.views.router_details import RouterDetailsViewSet
from api.views.login import LoginAuthToken
from django.urls import include, path, re_path

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"router-details", RouterDetailsViewSet)

urlpatterns = [
    re_path(r'login', LoginAuthToken.as_view()),
    re_path(r"^", include(router.urls)),
]
