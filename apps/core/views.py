from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from apps.core.pagination import ListPagination
from apps.core.custom_exception_handlers import get_response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseListModelMixin(ListModelMixin):

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return get_response(data=response.data, success=True)


class BaseRetrieveModelMixin(RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return get_response(
            data=response.data,
            success=True,
        )


class BaseCreateModelMixin(CreateModelMixin):

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return get_response(
            data=response.data,
            resource_created=True,
            headers=response.headers,
        )


class BaseUpdateModelMixin(UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return get_response(response.data, success=True)


class BaseDestroyModelMixin(DestroyModelMixin):

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return get_response(data=response.data, no_content=True)


class BaseViewset(
    BaseListModelMixin,
    BaseCreateModelMixin,
    BaseRetrieveModelMixin,
    BaseUpdateModelMixin,
    BaseDestroyModelMixin,
    GenericViewSet
):
    filter_backends = (OrderingFilter,)
    ordering_fields = ['id',]
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
