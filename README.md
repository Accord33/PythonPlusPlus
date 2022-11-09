# Python++ 公式ドキュメント

### Hello Worldを出力させてみよう!
---
Hello World!を実行してみましょう。

```ruby
#これはコメントアウトです
p("Hello World!");

#result
Hello World!
```
- Python++では```p```のあとはかならず()で囲います。
- セミコロンが必要です。

### 変数を使ってみよう!
---
変数に値を代入してみましょう。

```ruby
meg = "Hello World";
p(meg);

#result
Hello World!
```
- 変数と値を=でつなぎます。

### 四則計算をしてみよう!
---
和差積商を求めてみましょう。

基本演算子:```+ - * /```   
べき乗演算子:```**```   
インクリメント演算子:```++```

```ruby
#基本演算子
p(1 + 5);
p(5 - 1);
p(4 * 5);
p(6 / 3);

#result
6
4
20
2

#べき乗演算子
p(3 ** 4);

#result
81

#インクリメント演算子
num = 10;
num++;
p(num);

#result
11
```

- 可読性のため演算子と値には一つ以上のスペースを空けてください

### 条件分岐を使ってみよう!
---
分岐を作ってみましょう。

```ruby
num = 3;

#ここから分岐
if num > 0:
    p("numは0より大きいです");
else:
    p("numは0より小さいです");
end

#result
numは0より大きいです
```
- endはその処理の区切りを意味します。

### ループを使ってみよう!
---
While文でループを作ってみましょう。

```ruby
num = 1;

#ここからnumが10より小さい間繰り返す
while num < 10:
    p(num);
    #これを入れないと無限ループが始まってしまうので気を付けてください。
    num++;
end

#result
0
1
2
3
4
5
6
7
8
9
```

### 自作関数を作ってみよう!
---
特定の処理を呼び出す関数を作ってみましょう。
```ruby
func print_text():
    p("HELLO WORLD");
end

num = 0;
while num < 5:
    print_text();
    num++;
end

#result
HELLO WORLD
HELLO WORLD
HELLO WORLD
HELLO WORLD
HELLO WORLD
```

### import文を使ってみよう!
---
別ファイルの関数を実行してみましょう。

test1.ppp
```ruby
func test1():
    p("呼び出されました!");
end
```

test2.ppp
```ruby
import test1

p("一回目");
test1();
p("二回目");
test1();

#result
一回目
呼び出されました!
二回目
呼び出されました!
```

- ```import```の後に拡張子を抜いたファイル名を書くとそのファイルを読み込んでくれます。
