+++
title = "曲の管理"
date = 2023-03-28
[taxonomies]
categories = ["tech"]
tags = ["javascript", "gas"]
links = ["https://docs.google.com/spreadsheets/d/1LmRRIquxCkmebyrtUHs32l2HkXcTPOXd6-XmUoju8Hc/edit?usp=share_link"]
+++

<https://docs.google.com/spreadsheets/d/1LmRRIquxCkmebyrtUHs32l2HkXcTPOXd6-XmUoju8Hc/edit?usp=share_link>

spotifyとsoundcloudとyoutubeでfavoriteや再生リストに入れた曲を一括してまとめたいと思い試行錯誤しました｡

# 1. notionのdatabase
1. spotify apiでfavoriteした曲を取得し配列に格納する｡
2. notionのdatebaseを全て削除し上で用意した配列を行として追加していく｡
そんなプログラムなのですが2.がとにかく遅い｡更に218曲を追加したところで`notion_client.errors.RequestTimeoutError: Request to Notion API has timed out`と言われ終わってしまいました｡

# 2. notionのtable
ソートが出来ないらしいのでやめました｡

# 3. google spreadsheet + google apps script
## spotify
[api tokenのscopeの変更](https://github.com/spotify/web-api-examples)に戸惑っていたので少し時間を要しました｡
[コード](https://gist.github.com/natsuka-sili/61260528978acd324372e7fa38d34b5a)は半分くらいchat gptに書いてもらいました｡
## youtube
youtube apiの取得は簡単でした｡[コード](https://gist.github.com/natsuka-sili/288525dd437371a3e86c2feaa9709613)はほとんどchat gptに書いてもらいました｡

# 展望
## spreadsheet → web app
spreadsheetを良い感じに表示して更新できるwebアプリが作れたら便利になるだろうなと思っています｡

## soundcloud
最近の情報が無いなと思って簡単に調べたのですが
- apiの新規取得が停止中
- api自体が止まっている(?)
らしく諦めました｡spotifyと同じくらい使っていて実装したいので何とかなりませんかね｡