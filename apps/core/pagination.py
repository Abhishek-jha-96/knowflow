from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from apps.core.custom_exception_handlers import get_response
from apps.core.settings import PAGE_SIZE, MAX_PAGE_SIZE


class ListPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    max_page_size = MAX_PAGE_SIZE
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return get_response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            ),
            success=True
        )