from django.urls import path

from business.service.apis import asset as asset_api


urlpatterns = [
    path('service/ecs/create/', asset_api.CreateServiceAssetApi.as_view()),
    path('service/ecs/delete/', asset_api.DeleteServiceAssetApi.as_view()),
    path('service/ecs/list/', asset_api.ListServiceAssetApi.as_view()),
]
