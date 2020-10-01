```flow
st=>start: 処理開始
e=>end: 処理終了
io1=>inputoutput: データ入力
cond=>condition: 入力値が空
でない？
io2=>inputoutput: エラー出力
（※1）:>#footnote
sub1=>subroutine: 入力値の検証
（※2）:>http://www.google.com[blank]
op1=>operation: セッション開始

st->io1->cond
cond(yes)->sub1->op1->e
cond(no)->io2(right)->io1
​```