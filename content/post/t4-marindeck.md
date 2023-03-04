+++
title = "lualatexのluaの部分"
date = 2023-03-04
[taxonomies]
categories = ["tech"]
tags = ["lua", "latex"]
+++

<https://github.com/natsuka-sili/lualatex-scripting>

platexが悪く話題になった頃に触った[lualatex](http://www.luatex.org)ですが[lua](https://www.lua.org)が使える以外は特筆するような違いが無かったので[lua](https://www.lua.org)の使い道を考えた時のコードです｡

# フィボナッチ数のグラフ表示
[表示](https://github.com/natsuka-sili/lualatex-scripting/blob/main/fibonacci_graph.pdf)と[コード](https://github.com/natsuka-sili/lualatex-scripting/blob/main/fibonacci_graph.tex)

tikzpictureの形式で座標の文字列を出力する為に[lua](https://www.lua.org)を使っていますね｡これが出来ることからわかると思いますが大抵の事は出来ます｡出来ますが別に利点は大きくないかと思います｡

# フィボナッチ数の一覧表示
[表示](https://github.com/natsuka-sili/lualatex-scripting/blob/main/fibonacci_numerical.pdf)と[コード](https://github.com/natsuka-sili/lualatex-scripting/blob/main/fibonacci_numerical.tex)

形式とか考えずにただただ出力しています｡何も考えずに書けます｡わざわざgccとかをいれずにフィボナッチ数がわかるのは良い｡

# 三角関数表の作成
[表示](https://github.com/natsuka-sili/lualatex-scripting/blob/main/sin_table.pdf)と[コード](https://github.com/natsuka-sili/lualatex-scripting/blob/main/sin_table.tex)

表の形式で文字列を出力すれば良いですね｡数学のプリントの最後に三角関数表を付ける先生がいると思いますが[lua](https://www.lua.org)で作ることで雑談のネタにはなります｡

# 他
鉄緑の人って[lualatex](http://www.luatex.org)触ってるのかなと気になり数年ぶりに[ブログ](https://doratex.hatenablog.jp)を見に行ったらしっかりと触っていたしブログも定期的に書いていて感心してしまいました｡昔っから意味の分からない活用法を編み出している印象｡