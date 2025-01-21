from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



# 選手情報モデル
class Player(models.Model):
    POSITION_CHOICES = [
        ('投手', '投手'),
        ('内野手', '内野手'),
        ('外野手', '外野手'),
    ]
    player_name = models.CharField(max_length=30)
    team_name = models.CharField(max_length=30)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)  # 選択肢を追加   
    jersey_number = models.IntegerField(null=True, blank=True)  # 背番号
    birthplace = models.CharField(max_length=30) #出身地
    birthday = models.DateField()   # 誕生日
    height = models.IntegerField()  # 身長(cm)
    weight = models.IntegerField()  # 体重(kg)

    def __str__(self):
        return self.player_name


# 打者成績モデル
class BattingStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="batting_stats")
    year = models.IntegerField(validators=[MinValueValidator(1903), MaxValueValidator(2024)])  # 年を整数型に変更し、バリデータを追加
    team_name = models.CharField(max_length=50)
    avg = models.DecimalField(max_digits=5, decimal_places=3)# 打率
    games = models.IntegerField()  # 試合数
    at_bats = models.IntegerField()  # 打数
    hits = models.IntegerField()  # 安打数
    doubles = models.IntegerField()  # 二塁打
    triples = models.IntegerField()  # 三塁打
    home_runs = models.IntegerField()  # 本塁打
    total_bases = models.IntegerField()  # 塁打
    runs_batted_in = models.IntegerField()  # 打点
    runs_scored = models.IntegerField()  # 得点
    strikeouts = models.IntegerField()  # 三振
    walks = models.IntegerField()  # 四球
    hit_by_pitch = models.IntegerField()  # 死球
    sacrifices = models.IntegerField()  # 犠打
    sacrifice_flies = models.IntegerField()  # 犠飛
    stolen_bases = models.IntegerField()  # 盗塁
    on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3)  # 出塁率
    slugging_percentage = models.DecimalField(max_digits=5, decimal_places=3)  # 長打率
    OPS = models.FloatField()  # OPS
    class Meta:
        unique_together = ('player', 'year')  # playerとyearの組み合わせをユニークにする

    def __str__(self):
        return f"{self.player.player_name} - {self.year}"
    #関連するPlayerオブジェクトのplayer_nameフィールドを取得し、self.yearはこのBattingStatsオブジェクトのyearフィールドを取得します。
    # 最終的に、選手の名前と年をハイフンで区切った形式で表示します。


# 投手成績モデル
class PitchingStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="pitching_stats")
    year = models.IntegerField(validators=[MinValueValidator(1903), MaxValueValidator(2024)])  # 年を整数型に変更し、バリデータを追加
    team_name = models.CharField(max_length=50)
    era = models.DecimalField(max_digits=5, decimal_places=2)  # 防御率
    appearances = models.IntegerField()  # 登板
    complete_games = models.IntegerField()  # 完投
    shutouts = models.IntegerField()  # 完封
    wins = models.IntegerField()  # 勝利
    losses = models.IntegerField()  # 敗戦
    saves = models.IntegerField()  # セーブ
    win_percentage = models.DecimalField(max_digits=5, decimal_places=3)  # 勝率
    innings_pitched = models.FloatField() # 投球回
    hits_allowed = models.IntegerField()  # 被安打
    home_runs_allowed = models.IntegerField()  # 被本塁打
    strikeouts = models.IntegerField()  # 奪三振
    strikeouts_per_9 = models.DecimalField(max_digits=5, decimal_places=2) # 奪三振率
    walks_allowed = models.IntegerField()  # 与四球
    hit_batters = models.IntegerField()  # 与死球
    wild_pitches = models.IntegerField()  # 暴投
    balks = models.IntegerField()  # ボーク
    runs_allowed = models.IntegerField()  # 失点
    earned_runs = models.IntegerField()  # 自責点
    k_bb_ratio = models.DecimalField(max_digits=7, decimal_places=2)  # K/BB
    whip = models.DecimalField(max_digits=5, decimal_places=2)  # WHIP
    class Meta:
        unique_together = ('player', 'year')  # playerとyearの組み合わせをユニークにする

    def __str__(self):
        return f"{self.player.player_name} - {self.year}"


# 記事モデル
class Article(models.Model):
    article_title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_title


# コメントモデル
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."
