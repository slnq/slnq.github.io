+++
title = "zolaブログgithub pages公開"
date = 2023-02-27
[taxonomies]
categories = ["tech"]
tags = ["zola", "github-pages"]
links = ["https://natsuka-sili.github.io"]
+++

# zola
[ssg](https://en.wikipedia.org/wiki/Static_site_generator)の一種で[hugo](https://gohugo.io/)みたいなものだと思ってください｡[rust](https://www.rust-lang.org/ja)で書かれていますが別に[rust](https://www.rust-lang.org/ja)の知識は必要ありません｡[tera](https://tera.netlify.app)という[rust](https://www.rust-lang.org/ja)で書かれたテンプレートエンジンを使うのですが何となくで書けるので知識は不必要かと思います｡

# ブログを作る
[zolaの公式サイト](https://www.getzola.org/)を見ていけば最低限のブログは作れます｡わからないところは[テーマ](https://www.getzola.org/themes/)に色々な方の作ったサイトが載っていますのでそれを参考にしましょう｡

## taxonomies
恐らく問題になるのは[taxonomies](https://www.getzola.org/documentation/templates/taxonomies/)の実装かと思います｡テーマにあるサイトはタグやカテゴリの一覧が単独のページになっていることが多く他の方法を取ろうとするとコピペでは成り立ちません｡

私の目標としては
- テーマの一覧をトップページに載せる
- トップページで投稿を2つのカテゴリに分ける

だったので仕方なく[tera](https://tera.netlify.app)について調べたり色々試してなんとか実装しました｡詳しくは[githubの方](https://github.com/natsuka-sili/natsuka-sili.github.io)を見てほしいのですが詰まったところを書いておくと[index.htmlの4行目](https://github.com/natsuka-sili/natsuka-sili.github.io/blob/main/templates/index.html#L4)です｡

## カテゴリ分けで使うif文

`{% if page.taxonomies.categories == "tech" %}`と書いて失敗し続けて泣いていましたが[chatgpt](https://chat.openai.com/chat)に聞いたところ`{% if "tech" in page.taxonomies.categories %}`だよと優しく教えてくれて事なきを得ました｡

## パスの指定
私は[`../{{ term | safe }}`のような褒められたものではない指定をしている](https://github.com/natsuka-sili/natsuka-sili.github.io/blob/main/templates/tags/single.html#L10)のですが恐らく良くないので適当に良い方法を見繕ってください｡そして教えてください｡

## css
色を変数にしたかったのでsassにしましたが普通に作る分にはcssで良いと思います｡markdownをhtmlに変換したものが記事になるので`# h1`や`[リンク名](url)`を良い感じにcssで整える必要があります｡個人的には使う機能を予想して一気に作るよりは適宜作っていくほうが良いと感じています｡

# デプロイ
今回は[github pages](https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages)を使いました｡基本は[公式ドキュメント](https://www.getzola.org/documentation/deployment/github-pages/)に沿えば良いのですが知識不足と英語の苦手が故にまごついた部分があったのでメモしておくと
1. user icon>[Settings](https://github.com/settings/profile)>[Developer setting](https://github.com/settings/apps)>[Personal access tokens (classic)](https://github.com/settings/tokens)にて Generate new token(classic) を行い public_repo のみに印を付け発行されたtokenをコピーする
1. repositry>Settings>Secrets>ActionsにてNameにTOKENと書きSecretには先程コピーしたtokenをペーストする
1. /config.tomlをbase_url="https://'user_name'.github.io/'repository_name'"と書き換える
1. git pushした後でrepositry>Settings>Pages>SourceがDeploy from a branchでありrepositry>Settings>Pages>Branchがgh-pages /(root)になっている事を確認する

このような具合です｡

# 所感
[テーマ](https://www.getzola.org/themes/)が少ないのが[zola](https://www.getzola.org/)の最大の問題で次点で日本語の情報がほぼありません｡調べていないのでわかりませんが[hugo](https://gohugo.io/)なら自分で作らなくともタグ一覧を表示しカテゴリ分けが出来たのではないかなと思っています｡なので一切おすすめしません｡[rust](https://www.rust-lang.org/ja)だから早いとか言われていますが記事数が200程度なら変わらないと思います｡それでも[zola](https://www.getzola.org/)が使いたいなら[chatgpt](https://chat.openai.com/chat)の手を借りると良いと思います｡英語サイトの情報も内包していて適当な日本語で返してくれるので大体は解決します｡最新情報はbingのaiの方が良いのでしょうが適当なサイトから拾ってしまうために情報の質は[chatgpt](https://chat.openai.com/chat)の方が良い傾向にあると感じています｡

# 参考
- zolaの書き方を知るために参照\
<https://www.getzola.org>
- カテゴリのif文を教えてもらった\
<https://chat.openai.com/chat>
- ブログデザインを参照\
<http://saqum.com/index.html>
- 配色の参考\
<https://pigment.shapefactory.co/>
- タグマークの作成に参照\
<https://qiita.com/yuneco/items/444abd3f40d53ce7d078>
