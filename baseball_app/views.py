from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import login

from .models import Player, BattingStats, PitchingStats


# APIの取得コード
from .serializers import PlayerSerializer, BattingStatsSerializer, PitchingStatsSerializer

#⬇️DRFのビューセットクラスで、CRUD操作（Create, Read, Update, Delete）を自動で提供
class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()#操作対象となるデータを指定
    serializer_class = PlayerSerializer#データのシリアライズに使用するシリアライザーを指定

class BattingStatsViewSet(ModelViewSet):
    queryset = BattingStats.objects.all()
    serializer_class = BattingStatsSerializer

class PitchingStatsViewSet(ModelViewSet):
    queryset = PitchingStats.objects.all()
    serializer_class = PitchingStatsSerializer 



def index(request):
    return render(request, 'baseball_app/index.html')

# 選手プロフィール用ビュー
def player_profile(request):
    # プレイヤーデータを取得 (大谷選手を例として取得)
    player = get_object_or_404(Player, player_name="大谷翔平")

    # プレイヤーに関連する打者成績と投手成績を取得
    batting_stats = BattingStats.objects.filter(player=player).order_by("-year")
    pitching_stats = PitchingStats.objects.filter(player=player).order_by("-year")

    # テンプレートに渡すコンテキストデータ
    context = {
        "player": player,
        "batting_stats": batting_stats,
        "pitching_stats": pitching_stats,
    }

    return render(request, "baseball_app/player_profile.html", context)
def baseball_basics(request):
    return render(request, 'baseball_app/baseball_basics.html')

def contact(request):
    return render(request, 'baseball_app/contact.html')