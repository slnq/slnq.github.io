+++
title = "rust→wasm電界シミュレータ"
date = 2023-03-02
[taxonomies]
categories = ["tech"]
tags = ["rust", "wasm", "github-pages"]
links = ["https://natsuka-sili.github.io/werve-wasm/"]
+++

# 心意気
卒業研究として[gpu.jsで電界シミュレータを作っている](../post/t2-werve-gpujs)間に[webassembly](https://webassembly.org)というものを知ってしまいそれ以降はやる気が低下しきりながらもなんとか[gpu.js](https://gpu.rocks/#/)で作り終わり時間も手に入れたのでいよいよ[webassembly](https://webassembly.org)で作り始めました｡

# 作ったもの
<https://natsuka-sili.github.io/werve-wasm/>
## 機能
黒い範囲をクリックすると白いぼやけた円が表示されるかと思います｡これはスライダーに応じたcharge valueの左ある数字の大きさに対応した電荷です｡このように電荷をいくつか置き輝度で電界を見て楽しめます｡また上にあるスイッチの説明を以下に示します｡

| install | : | クリックするとchargeに合う値の電荷を置きます |
| -: | | |
| remove | : | 電荷をクリックすると消すことができます |
| control | : | 電荷をドラッグアンドドロップで移動させられます |
| fix | : | 電荷をクリックすると固定できます |

## ソースコード
<https://github.com/natsuka-sili/werve-wasm>

基本的に`src`内の`.rs`ファイルを読んでもらえばシミュレーションについてわかるかと思います｡

# 処理
1. 1つの電荷に対する電界の値を1539×1539で計算しテンプレートに格納する
1. 電荷の位置を元に電界のテンプレートを動かし配列769×769に格納する
1. 電荷の数だけ総和して配列769×769に格納していく
1. 電荷の座標に対応する電界配列の要素を電荷値と乗算してクーロン力を計算する
1. クーロン力を元に位置と速度と加速度を計算する
1. 表示する

これの2.から6.を繰り返していると思ってください｡配列の大きさ769×769の理由はよく覚えていないのですが奇数の方が都合が良いというのは確かです｡

## rust→wasm
入力と表示以外の全てを[rust](https://www.rust-lang.org/ja)から変換した[wasm](https://webassembly.org)で実行しています｡[wgpu](https://wgpu.rs)や[webgpu](https://www.w3.org/TR/webgpu/)は仕様が変わり続けているので使っていません｡表示に適すような配列への変換もこっちで行っています｡

## canvas
上述にある表示に適すような配列を共有メモリーから表示しています｡[gpu.js版](https://github.com/natsuka-sili/werve-gpujs)にあったベクトル表示を未だに作っていないためcanvasは1枚のみでの実装です｡

## css
~~何も無いのでスマートフォンから使おうとすると電荷を動かす時にスクロールされるなど使いにくいと思います｡pc(2060)では[wasm版](https://github.com/natsuka-sili/werve-wasm)の方がフレームレートが出たのですがスマートフォン(iphone8)では[gpu.js版](https://github.com/natsuka-sili/werve-gpujs)の方が出たのでcssを作る気が消えたと記憶しています｡しかしiphone11で試したところ[wasm版](https://github.com/natsuka-sili/werve-wasm)もかなり良く動いたのでやる気によってはcssやベクトル表示機能を作ると思います｡~~

[chat gptに良い感じのものを作ってもらいました｡](https://poe.com/s/XGTlkiRiyR4deC8lfmIx)

# デプロイ
[webpack](https://webpack.js.org/)を用いてローカルで生成したものを[github pages](https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages)で`/docs`のデプロイしています｡