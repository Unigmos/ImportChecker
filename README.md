# ImportChecker
本日の予定(講義内容)を通知するプログラム

## 機能
プログラム実行時、Excelに格納された予定表を参照し、本日の予定として通知を行うプログラムです。<br>
batファイルを用いて、タスクスケジューラに登録することで起動時に本プログラムを実行させることも可能です。<br>
<br>
※最初にtime.sleep()を用いている理由は、画面表示前にプログラムが実行されてしまうためです。<br>
time.sleep()を用いることで画面が表示されてから通知を行うことが可能になります。

## ざっくりとした仕組み
ファイル読み込み(現在はxlsxファイルのみ対応)<br>
↓<br>
通知内容作成<br>
↓<br>
通知処理<br>

## 起動時に動かしたい場合
batファイル「Call_TodaysSchedule_Demo.bat」に自身のPython.exeとpyファイルのパスを指定し、タイムスケジューラに設定します。<br>


## 動かない場合
・実行できない！<br>
→Python実行環境がない可能性があります。Pythonの実行環境を用意してください。<br>
・ModuleNotFoundとなる<br>
→pip等でライブラリのインストールを行ってください。<br>
今回用いたライブラリはこちら(標準ライブラリを含みます)↓
| ライブラリ名     | 導入目的                       |
|:-----------------|:-------------------------------|
| time             | 処理の一時停止                 |
| sys              | 処理の終了                     |
| openpyxl         | Excelファイルの参照            |
| csv              | Csvファイルの参照              |
| numpy            | 配列の調整を行う               |
| datetime         | 曜日情報の取得                 |
| pathlib          | パスの拡張子確認               |
| plyer            | 通知を行う                     |

## お問い合わせ<br>
何かございましたら「shaneron@sumahotektek.com」まで連絡ください。反応は非常に遅いです。<br>

### 変更履歴<br>
Ver1.0:初期バージョン<br>
Ver1.1:csvファイルに対応させました<br>
Ver1.2:アイコンを自作の画像に置き換えました<br>
Ver1.3:命名規則に則って変数や定数の表記を変更しました。<br>