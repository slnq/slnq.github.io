+++
title = "iosのyoutube視聴環境"
date = 2022-12-28
[taxonomies]
tags = ["ios", "youtube"]
+++

pcが無い外出先ではiphoneを用いて配信を観る訳だがappleとyoutubeの制約で快適とは言い難い\
少し工夫すれば改善されるので私の環境を紹介する

###

[youtube liveを検索するショートカット](https://www.icloud.com/shortcuts/88db34d60850401c9f4766660e8ffc04)で配信を検索する\
[nijimado](https://niji-mado.web.app/home)やtlなどから飛ぶ事も多いが新しい人を発掘する時も多く使う機会は少なくない

配信を開いたらpicture in picture機能のbookmarkletを実行する
~~~
javascript:(v=%3E%7Bv=document.querySelector('video');v.addEventListener('webkitpresentationmodechanged',e=%3Ee.stopPropagation(),true);setTimeout(()=%3Ev.webkitSetPresentationMode('picture-in-picture'),1000);%7D)();
~~~

[youtube liveのチャットを表示するショートカット](https://www.icloud.com/shortcuts/4ace49a63aae4f4082d024c35f4bcd5c)を実行しチャット欄と配信を観られるようにする

###

これでpcと同じuiのチャットを見られるようになったのだがtwitterと同時に見られないのが問題\
仕方ないので定期的にsafariとtwitterを行き来しているが同時に見られないというのは寂しいもので
