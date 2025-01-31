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
    path('baseball-basics/', views.baseball_basics, name='baseball_basics'), #野球の基礎
    path('news/', views.news_list, name='news_list'),  #ニュース一覧ページ
    path('news/<int:pk>/', views.news_detail, name='news_detail'), #ニュース詳細ページ
    path('news/<int:pk>/comment/edit/<int:comment_pk>/', views.edit_comment, name='edit_comment'), #コメント編集
    path('news/<int:pk>/comment/delete/<int:comment_pk>/', views.delete_comment, name='delete_comment'),  # コメント削除
    path('news/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),  # お気に入り追加/削除
    path('favorites/', views.favorite_list, name='favorite_list'),  # お気に入り一覧
    path('contact/', views.contact, name='contact'),  # お問い合わせ
]

