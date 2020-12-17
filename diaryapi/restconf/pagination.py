from rest_framework import pagination


class DiaryAPIPagination(pagination.LimitOffsetPagination):
    # page_size = 20
    max_limit = 20
    default_limit = 10
    # limit_query_param = 'lim'
