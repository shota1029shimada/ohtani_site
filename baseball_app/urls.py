from django.urls import path, include
from . import views
#API
from rest_framework.routers import DefaultRouter #DRFの「ルーター」
from .views import PlayerViewSet, BattingStatsViewSet, PitchingStatsViewSet
#ビューセット（PlayerやBattingStatsのAPIロジックを記述したクラス）をインポート

router = DefaultRouter() #ビューセットを簡単に登録(URLパターンを簡潔に自動生成)
router.register('players', PlayerViewSet)
router.register('batting-stats', BattingStatsViewSet)
router.register('pitching-stats', PitchingStatsViewSet)

app_name = 'baseball_app'

urlpatterns = [
    path('api', include(router.urls)),#API
    path('', views.index, name='index'),  # トップページ
    #path('highlights/', views.highlights, name='highlights'),  # ハイライト
    path('player-profile/', views.player_profile, name='player_profile'),  # 大谷選手情報ページ
    path('baseball-basics/', views.baseball_basics, name='baseball_basics'),  # 野球の基礎
    #path('news', views.news, name='news'),  #ニュース
    path('contact/', views.contact, name='contact'),  # お問い合わせ
]

