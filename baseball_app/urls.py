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

urlpatterns = [
    path('', include(router.urls)),
]
