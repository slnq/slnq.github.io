+++
title = "ブログを作る zolaを用いて"
date = 2022-12-25
[taxonomies]
tags = ["web", "zola"]
+++

[hugo](https://gohugo.io/)でも[jekyll](http://jekyllrb-ja.github.io/)でも無く[zola](https://www.getzola.org/)を選んだ理由は多少[rust](https://www.rust-lang.org/ja)を触ったことがあるというものだが一切の利点は無かった

テーマを使わなかった理由はタグ機能があり常に一覧表示されているシンプルなものが見つからなかったからだが結果的には良き選択だったと思える

ssgどころかwebの初心者である私が躓いた点について書く

## 変数の利用とtaxonomies機能と
[テーマ](https://www.getzola.org/themes/)を5つくらい見ながら何とか使える程度にはなったが一切の理解はしていない

もし[zola](https://www.getzola.org/)を使いたいweb初心者がいた時のために見れば使い方だけはわかるようになれそうな[テンプレート](https://github.com/natsuka-sili/zola-test)を置いておく

## [github pages](https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages)への公開について
基本は[公式ドキュメント](https://www.getzola.org/documentation/deployment/github-pages/)に沿えば良いのだが知識不足と英語の苦手が故にまごついた部分の流れについて下記の通り
1. user icon>[Settings](https://github.com/settings/profile)>[Developer setting](https://github.com/settings/apps)>[Personal access tokens (classic)](https://github.com/settings/tokens)にて Generate new token(classic) を行い public_repo のみに印を付け発行されたtokenをコピーする
1. repositry>Settings>Secrets>ActionsにてNameにTOKENと書きSecretには先程コピーしたtokenをペーストする
1. /config.tomlをbase_url="https://'user_name'.github.io/'repository_name'"と書き換える
1. git pushした後でrepositry>Settings>Pages>SourceがDeploy from a branchでありrepositry>Settings>Pages>Branchがgh-pages /(root)になっている事を確認する

## 
色々と戸惑ったが及第点といった具合のブログが作れて良かった

というわけで\
[**私のアツいブログ活動！ブロカツ！始まります！ﾌﾌｯﾋ**](https://dic.nicovideo.jp/a/%E3%83%95%E3%83%95%E3%83%83%E3%83%92)