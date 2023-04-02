+++
title = "githubのcontribution パクる"
date = 2023-04-02
[taxonomies]
categories = ["tech"]
tags = ["javascript", "github-pages"]
links = ["https://gist-4d0c6.web.app/like_contribution.html"]
+++

[コード](https://gist.github.com/natsuka-sili/5c6407c9173c67b2222fa837cd9ce735)

# githubのcontribution 通称 草
緑色だからか草と称されている`N contributions in the last year`のことです｡
githubのプロフィールページから見ることが出来ます｡

これをパクってツイート件数に応じて緑色の濃度を操ろうと思いました｡

# twitter apiの変更
これを作ろうと思ったのが3月27日あたりでした｡[参考サイト](https://adrianroselli.com/2018/02/github-contributions-chart.html)も見つけ作り始めたと同時にtwitter apiの変更内容が通達されました｡
無料ではツイートの取得が出来ないようです｡
丁度二次元配列`[[年月日, contribution数],...]`からgithubの旧contributionをjavascriptで生成するところまでは行っておりました｡いよいよtwitter apiでデータを取得するぞと意気込んでいた時でしたから大層残念でした｡
1ヶ月ほどは使えるようですが最後まで作るかは微妙です｡

# 現状のもの
<https://gist-4d0c6.web.app/like_contribution.html>

こんな感じです｡DOM操作を大量に行っているのですが特に重くなく実装できるのですね｡

# 展望
[misskey](https://misskey.io/@sq)に移り完成させるのもありかと思ったのですが実はheatmapという名で既に実装されているのですよね｡どうしましょうね｡

一応気象庁からデータを受け取り毎日更新するのもありなのですが毎日1年分を受け取ると良くないので適当な改良が必要で今すぐには実装できませんね｡