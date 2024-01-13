from django.urls import path
from blogging.views import stub_view, list_view_v2

urlpatterns = [
    path('', list_view_v2, name="blog_index"),
    path('posts/<int:post_id>/', stub_view, name="blog_detail"),
]
