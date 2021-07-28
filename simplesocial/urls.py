
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('test/', views.TestPage.as_view(), name="test"), # rename to welcome
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('posts/', include("posts.urls", namespace="posts")),
    path('groups/',include("groups.urls", namespace="groups")),
    path('api/posts/', include("posts.api.urls", namespace="postsApi")),
    path('api/groups/', include("groups.api.urls", namespace="groupsApi")),
]
