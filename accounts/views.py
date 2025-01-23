from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm#ユーザー作成用のフォーム
from django.contrib.auth import login#正常に登録されたら自動的にログイン

def signup(request):
    if request.method == 'POST':#POSTの場合、ユーザーがフォームを送信した
        form = UserCreationForm(request.POST)#送信されたデータをフォームにバインド
        if form.is_valid():#データが正しいかどうかをチェック
            form.save()  # ユーザーをデータベースに保存
            return redirect('login')  # ログインページにリダイレクト
    else:#POSTでない場合（通常は'GET'）、新しい空のUserCreationFormを作成
        form = UserCreationForm()  # 空のフォームを作成
    return render(request, 'accounts/signup.html', {'form': form})
                                  #signup.htmlテンプレートをレンダリング