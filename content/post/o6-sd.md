+++
title = "sd生成環境"
date = 2023-04-03
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

# webui用extensionのインストール


# モデルのダウンロード
1. `seait\stable-diffusion-webui\models\Stable-diffusion`に`.ckpt`や`.safetensor`といったモデルをダウンロード
1. vaeやembeddingsやloraやcontrolも同様にダウンロード
1. comfy uiでモデルを使えるようにするために