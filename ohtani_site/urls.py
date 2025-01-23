from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),#管理画面
    path('accounts/', include('django.contrib.auth.urls')),  # デフォルトの認証システム
    path('accounts/', include('accounts.urls')), #accountsディレクトリに移動
    path('baseball/', include('baseball_app.urls')), #baseball_appディレクトリの移動
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 開発環境でのメディアファイル配信用

#'django.contrib.auth.urls'➡️Djangoが提供するログイン・ログアウト機能を使う