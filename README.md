# AutoProgramCheckerByCopilot
プログラムの実行結果をcopilotが都度述べるコードです。
test.pyの中に開発中のコードを書いてください。
実行時はpython sub.pyを実行してください。すると、observetest.pyとtest.pyが実行されます。

各コードの解説
test.py->実行が成功（標準出力）したときは各コードの解説を、失敗（標準エラー）したときはコードの改善場所をcopilotが解説します。初期設定はコロンがないのでエラーが出るはずです。適当にいじって挙動を確認してください。
sub.py->test.py,dev.pyを実行します。
dev.py->pyautoguiを用いてcopilotに説明させます。


