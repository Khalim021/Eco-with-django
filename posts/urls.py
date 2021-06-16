from django.urls import path

from posts.views import PostsListView, PostDetailView, CommentCreateView

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('', PostsListView.as_view(), name='list'),
]



