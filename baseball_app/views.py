from rest_framework.viewsets import ModelViewSet
from .models import Player, BattingStats, PitchingStats





""""" APIの取得コード
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
    serializer_class = PitchingStatsSerializer """