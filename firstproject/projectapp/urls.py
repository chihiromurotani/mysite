from django.urls import path
from .views import(
    TopView,RegistUserView,UserLoginView,UserLogoutView,CategoryListView,RegistCategoryView,
    ItemGetListView,CategoryUpdateView,CategoryDeleteView,RegistItemView,ItemUpdateView,
    ItemDeleteView,ItemDetailView
    )

app_name = 'projectapp'
urlpatterns = [
    path('top/',TopView.as_view(),name='top'),
    path('regist/',RegistUserView.as_view(),name='regist'),
    path('user_login/',UserLoginView.as_view(),name='user_login'),
    path('user_logout/',UserLogoutView.as_view(),name='user_logout'),
    path('category_list/',CategoryListView.as_view(),name='category_list'),
    path('category_regist/',RegistCategoryView.as_view(),name='category_regist'),
    path('category_update/<int:pk>',CategoryUpdateView.as_view(),name='category_update'),
    path('category_delete/<int:pk>',CategoryDeleteView.as_view(),name='category_delete'),
    path('item_get_list/<int:category_id>',ItemGetListView.as_view(),name='item_get_list'), 
    path('item_regist/<int:category_id>',RegistItemView.as_view(),name='item_regist'),
    path('item_update/<int:pk>',ItemUpdateView.as_view(),name='item_update'),
    path('item_delete/<int:pk>',ItemDeleteView.as_view(),name='item_delete'),
    path('item_detail/<int:pk>',ItemDetailView.as_view(),name='item_detail'),
]