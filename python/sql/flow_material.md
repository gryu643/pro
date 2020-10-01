```flow
st=>start: 処理開始
e=>end: 処理終了
op1=>operation: .batファイルダブルクリック
op2=>operation: > python guidata.pyを実行
op3=>operation: GUI表示
op8=>operation: ファイルシステムでcsv選択
op9=>operation: csvをdbファイルにインポート
op11=>operation: データベース検索
io1=>inputoutput: 物品コード入力
io2=>inputoutput: カナ品名入力
io3=>inputoutput: 組織コード入力
io4=>inputoutput: 組織名入力
cond1=>condition: 物品コードで検索
クリック
cond2=>condition: カナ品名で検索
クリック
cond3=>condition: 組織コードで検索
クリック
cond4=>condition: 組織名で検索
クリック
cond5=>condition: csvインポート
クリック
cond7=>condition: 終了ボタン
クリック
cond8=>condition: ファイル選択したか

st->op1->op2->op3->cond7
cond7(yes)->e
cond7(no)->cond5
cond5(yes)->op8->cond8
cond8(yes)->op9(right)->cond7
cond8(no)->cond7
cond5(no)->cond1
cond1(yes)->io1->op11(right)->cond7
cond1(no)->cond2
cond2(yes)->io2->op11(right)->cond7
cond2(no)->cond3
cond3(yes)->io3->op11(right)->cond7
cond3(no)->cond4
cond4(yes)->io4->op11(right)->cond7
cond4(no)->cond7
```