from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
  path('start/', start_view, name='start'),
  path('login/', login, name="login"),
  path('logout/', logout, name='logout'),
  path('signup/', signup, name='signup'),
  path('mypage/<int:id>/', mypage, name='mypage'),
  path('mypage/<int:id>/likes/', my_likes, name='my_likes'),
  path('mypage/<int:id>/visits', my_visits, name='my_visits'),
  path('mypage/<int:id>/reviews', my_reviews, name='my_reviews'),
  path('edit-profile/', edit_profile, name='edit_profile'),
  path('unlike/<int:menu_id>/', unlike_menu, name='unlike_menu'),
#path('upload-profile/', upload_profile_image, name='upload_profile_image'), #프로필사진 업로드

  #path('mypage/<int:id>/rice-map/', rice_map_view, name='rice_map'),
]