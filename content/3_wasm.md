+++
title = "電界シミュレーションwasm"
date = 2022-12-27
[taxonomies]
categories = ["tech"]
tags = ["javascript", "rust", "wasm"]
+++

[電界シミュレーション](../2-sotsuken)をwasmで実装しようという心意気による\
今年の初めには年内に[webgpu](https://www.w3.org/TR/webgpu/)が来るだろうと思い作っていたが夏頃には[sca自](https://twitter.com/sca_di)みたいなものだと気づき開発を止めた為に途中だが最低限は動く

<https://natsuka-sili.github.io/werve/>

[gpujs版](https://s1kl.github.io/werve/)に対してpcでは安定しているがiOS端末では逆にカクつく印象がある\
私のpcも一応rtx3060のっているのですが

[webgpu](https://www.w3.org/TR/webgpu/)が正式実装されて[wgpu](https://wgpu.rs/)が対応したら制作も再開しようかなとの意気込み
