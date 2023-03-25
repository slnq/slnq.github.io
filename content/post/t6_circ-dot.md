+++
title = "円状のドットへ画像加工"
date = 2023-03-24
[taxonomies]
categories = ["tech"]
tags = ["javascript", "firebase"]
links = ["https://circ-do.web.app"]
+++

# aiに書いてもらうという流行り
現在のtwitter上では大規模言語モデルにプログラムを書いてもらい褒めるもしくは貶すという一連の行動が流行しています｡
github copilot xでどこまで状況が変わるか心底楽しみです｡

# 実際に書いてもらう
<https://poe.com/s/xfu6DF3SdqxCSpFhIEnq>

様子は上の通り｡図書館学が好きな人はstep-by-stepをつければ良いのにとでも思うのでしょうか｡

<https://circ-do.web.app>

完成したサイトは上のもの｡スマホで使えるようにhtmlとcssを多少触りましたが他はchat gptの通りです｡
確かに良くできていますね｡元となるコードがあったのかは調べていないのでわかりませんが｡

<https://gist.github.com/natsuka-sili/925eda31999a88c527170377a1d6478b>

コードは上の通り｡無駄なループをしていそうですが手を加えるくらいなら最初からrust→wasmで書くような内容なので手直しをする気もありません｡
では何故wasmでaiに書いてもらわないのかこれが肝要で試してみたらうまくいきそうも無かったというところです｡
一度javascriptで書かせたプログラムを渡してcやrustで書くように指示して...といった段階を踏めば出来るのかもしれません｡ただそうまでするなら自分で全部書くような簡単な処理なので今回は一任しました｡

私の指示でcanvasを2つ使うようにしてaiにもわかりやすく指示しているあたり多少はhtmlに慣れていないと出来ないかもしれませんが他の部分に関してはプログラミングを知らない人でも簡単にできそうです｡

# firebaseを使ってみる
さて今回はhtmlファイルにstyleもscriptも書き込んでいる為にリポジトリを作りたくなくgithub pagesを使うか悩みました｡結局firebase hostingならgithub連携やリポジトリ無しで使えるとchat gptが教えてくれたのでこれを選びました｡brewでfirebase cliを落とすのに相当な時間がかかった以外は簡単で便利ですね｡