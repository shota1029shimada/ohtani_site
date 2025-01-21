from django.contrib import admin
from .models import Player, BattingStats, PitchingStats, Article, Comment

#@はただの関数に等しいもので、後に続く関数をパラメーターとして受け取り、役割を引き継ぐ

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):#Playerモデルの管理画面のカスタマイズに使われる
    list_display = ('player_name', 'team_name', 'position', 'jersey_number')
    search_fields = ('player_name', 'team_name')
    list_filter = ('position', 'team_name')

@admin.register(BattingStats)
class BattingStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'team_name', 'avg', 'home_runs')
    search_fields = ('player__player_name',)
    list_filter = ('year', 'team_name')

@admin.register(PitchingStats)
class PitchingStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'team_name', 'era', 'wins', 'strikeouts')
    search_fields = ('player__player_name',)
    list_filter = ('year', 'team_name')

admin.site.register(Article)
admin.site.register(Comment)

#list_display➡️一覧画面で表示するフィールドを指定
#search_fields➡️検索可能なフィールドを指定
#list_filter➡️サイドバーに表示されるフィルタを指定