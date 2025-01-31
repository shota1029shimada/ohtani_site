from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import login
from .models import Player, BattingStats,PitchingStats,Article,Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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


#トップページに移動
def index(request):
    return render(request, 'baseball_app/index.html')#名前空間/urlのnameを指定

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

#野球の基礎
def baseball_basics(request):
    return render(request, 'baseball_app/baseball_basics.html')

#ニュース一覧ページ
def news_list(request):
    articles = Article.objects.all().order_by('-created_at')  # 記事を作成日順で取得
    return render(request, 'baseball_app/news_list.html', {'articles': articles})

#ニュース詳細ページ
def news_detail(request, pk):#記事のpkを受け取る
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()# 記事に関するコメントをarticleテーブルからデータをすべて取得
    is_favorited = request.user in article.favorites.all() if request.user.is_authenticated else False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():#フォームが送信されたら、CommentFormで入力内容を検証
            comment = form.save(commit=False)
            comment.article = article  # コメントをこのニュース記事に関連付け
            comment.user = request.user  # コメント投稿者をログイン中のユーザーに設定
            comment.save()
            return HttpResponseRedirect(reverse('news_detail', args=[pk]))
    else:
        form = CommentForm()

    return render(request, 'baseball_app/news_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
        'is_favorited': is_favorited
    })

#コメント編集
def edit_comment(request, pk, comment_pk): 
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk, article=article)

    # 投稿者でない場合はアクセスを拒否
    if comment.user != request.user:
        return redirect('baseball_app:news_detail', pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('baseball_app:news_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'baseball_app/edit_comment.html', {
        'form': form,
        'article': article,
        'comment': comment
    })

#コメント削除
def delete_comment(request, pk, comment_pk):
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk, article=article)

    # 投稿者でない場合はアクセスを拒否
    if comment.user != request.user:
        return redirect('baseball_app:news_detail', pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('baseball_app:news_detail', pk=pk)

    return render(request, 'baseball_app/delete_comment.html', {
        'article': article,
        'comment': comment
    })

#お気に入り追加/削除の処理 
@login_required
def toggle_favorite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.favorites.all():
        article.favorites.remove(request.user)  # お気に入りから削除
        favorited = False
    else:
        article.favorites.add(request.user)  # お気に入りに追加
        favorited = True
    return JsonResponse({'favorited': favorited})

#お気に入り一覧の表示
@login_required
def favorite_list(request):
    favorites = request.user.favorite_articles.all()
    return render(request, 'baseball_app/favorite_list.html', {'favorites': favorites})

    
def contact(request):
    return render(request, 'baseball_app/contact.html')

