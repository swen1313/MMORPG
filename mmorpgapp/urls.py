from django.urls import path

from .views import IndexView, AdvertList, AdvertDetail, ResponseList, ResponseDetail, AdvertUpdateView, RListView, ResponseDeleteView

urlpatterns = [
    path('', IndexView.as_view()),
    path('advertlist', AdvertList.as_view(), name='advert_list'),
    path('advertlist/<int:pk>', AdvertDetail.as_view(), name='advert_detail'),
    path('responselist', ResponseList.as_view(), name='response_list'),
    path('rlistview', RListView.as_view(), name='rlistview_list'),
    path('responselist/<int:pk>', ResponseDetail.as_view(), name='response_detail'),
    path('advertlist/<int:pk>/new', AdvertUpdateView.as_view(), name='advert_update'),
    path('responselist/<int:pk>/delete', ResponseDeleteView.as_view(), name='response_delete'),

]



