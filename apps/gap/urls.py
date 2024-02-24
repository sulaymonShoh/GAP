from django.urls import path

from apps.gap.views import RoomListView, RoomDetailView, LikeOpinionView, OpinionDetailView

app_name = 'gap'
urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('rooms/opinions/<int:pk>/', OpinionDetailView.as_view(), name="opinion_detail"),
    path('rooms/<pk>', RoomDetailView.as_view(), name='room'),
    path('like/<pk>', LikeOpinionView.as_view(), name='opinion-like')

]
