from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
    path('user/', include('cat_user.urls')),
    path('wallet', include('cat_wallet.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth', views.obtain_auth_token)
]