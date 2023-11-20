from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('user/', include('cat_user.urls')),
    path('wallet', include('cat_wallet.urls')),
    path('admin/', admin.site.urls),
]