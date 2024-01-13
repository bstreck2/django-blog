from django.urls import path
from blogging.views import stub_view, list_view_v2, detail_view

urlpatterns = [
    path('', list_view_v2, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
