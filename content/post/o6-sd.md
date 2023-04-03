+++
title = "sd生成環境"
date = 2023-04-04
[taxonomies]
categories = ["other"]
tags = ["stable-diffusion"]
links = []
+++

# Super Easy AI Installer Toolをインストール
1. <https://github.com/diStyApps/seait/releases>からseait_installers_version_x.x.x.zipをダウンロードし解凍
1. seait.exeを実行
1. pythonとgitが入っていない場合はseaitの中からインストール(seaitからpythonをインストールしてpathを通してもnoneのままになっている場合もあるが問題はない)

# webuiのインストール
1. automatic1111 webuiをインストール
1. comfy uiをインストール
1. controlnet + t2i - webui extensionをインストール(seaitを使えばwebuiのextensionからダウンロードしなくてよい)

# モデルのダウンロード
1. `seait\stable-diffusion-webui\models\Stable-diffusion`に`.ckpt`や`.safetensor`といったモデルをダウンロード
1. `\models\VAE`や`\models\lora`や`\embeddings`や`\extensions\sd-webui-controlnet\models`も同様にダウンロード
1. comfy uiでモデルを使えるようにするために[シンボルリンクを作成するバッチファイル](https://gist.github.com/natsuka-sili/ad219b5592b207a0ec06bd7955ad719e)を作る(取り敢えずmodel var lara embedding controlnetのみをリンクしている)

# webuiの確認
1. webuiで出力のテスト(embeddingやcontrolnetやloraをオンオフしながら)
1. 同様にcomfyuiもテスト(seedを同じにしたところでノイズの生成手法がwebuiとは異なるので画像は一致しない)

# comfyuiの所感
ダウンロードしてから軽いテストしかしていないが
- controlnetやloraを複数かけられる
- hires fixで異なるsamplerを使える
- webuiより軽い
- ノードuiなので処理が追いやすく理解しやすい

との利点を感じた｡area composition及びnoisy latent compositionも強みであると思うので追って触りたい｡

あとclip text encodeのフォントが見にくいのでstyle.cssに
```
textarea{
	font-family: sans-serif;
}
```
というような追記をしたほうが良いと思う｡