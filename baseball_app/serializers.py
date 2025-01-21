#、PythonのオブジェクトとJSON（またはその他のフォーマット）の間でデータをシリアライズ（序列化）および
# デシリアライズ（逆序列化）するためのクラス を定義するファイルです。

#モデルのデータをJSON形式に変換するため
"""""
from rest_framework import serializers
from .models import pip install requests beautifulsoup4

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'# すべてのフィールドをシリアライズ(序列化）

class BattingStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattingStats
        fields = '__all__'

class PitchingStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PitchingStats
        fields = '__all__'      
        """