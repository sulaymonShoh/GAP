from django.urls import path

from apps.gap.views import RoomListView, RoomDetailView, LikeOpinionView, OpinionDetailView, CommentOpinionView, \
    OpinionCreateView

app_name = 'gap'
urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('rooms/opinions/create/', OpinionCreateView.as_view(), name="opinion_create"),
    path('rooms/opinions/<int:pk>/', OpinionDetailView.as_view(), name="opinion_detail"),
    path('rooms/<pk>', RoomDetailView.as_view(), name='room'),
    path('rooms/opinions/like/<pk>', LikeOpinionView.as_view(), name='opinion_like'),
    path('rooms/comments/like/<pk>', CommentOpinionView.as_view(), name='comment_like'),

]
