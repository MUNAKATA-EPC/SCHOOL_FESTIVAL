# SCHOOL_FESTIVAL
文化祭で使用したプログラムです

PS3コントローラーの受信に関して

http://gijin77.blog.jp/archives/21966552.html

上記のWEBサイトを参考にしました。使用するESP32ライブラリに関してVer1.0.4以外のバージョンで動作確認が取れません。専用ソフトを使用して使用するM5stampのMACaddressをコントローラーに書き込む必要があります。Ps3.data.---の戻り値がスティックの角度となります。

Wii Balance Bordに関して

https://github.com/takeru/Wiimote/tree/BalanceBoard

上記のWEBサイトを参考にしました。ライブラリをインストールしてサンプルプログラムを実行します。weight［ーーー］の戻り値が各センサの重量となります。起動時に本体裏のリセットボタンを押す必要があります。
