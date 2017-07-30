# Python 最速文法

# 参考

# みんなのPython 第3版

# [python] 年末大感謝祭！初心者脱出のためのPythonTipsを50個紹介
# http://kwatch.houkagoteatime.net/blog/2013/12/07/python-tips/

# エンコード指定
# -*- coding: utf-8 -*-


# コードの区切り＝;（セミコロン）


# モジュールのインポート
import moduleName
from moduleName import functionName

from math import *  # import all functions
from math import e
from math import e as newName
from math import (e, pi) # 複数インポートするなら括弧で囲む

## from文を使うとモジュール名省略可能になる
import math
math.sin(60)

from math import sin
sin(60)

## モジュールファイルの作成
## (スクリプトファイルをそのままモジュールとして利用可)

# 1. moduleName.py に関数を書く
# 2. import moduleName


# 行の途中で改行したい： 行末にバックスラッシュ (\)
import urllib, poplib, sys, calendar, \
    datetime, re


# リテラル
b = 0b1000  # 2進数
c = 0x1ff   # 16進数

# Bool型
True
False

# Null
None


# シンボルの大文字と小文字は区別される
python = 100
Python = 200
print(python, Python) #=> 100 200


# 標準出力への出力(改行つき)
print("abc")
print("abc", "def") # 半角スペースで連結
print("abc", file=sys.stderr)   # 標準エラー出力

# 改行なしで連結
for i in range(10):
    print("abc", end = ' ') #=> abc abc abc abc abc abc abc abc abc abc


# 標準入力からの取得
s = raw_input()
#s = input()     # == eval(raw_input())


# 四則演算
x += 1
x -= 1
x *= 1
x /= 1

x = 2 ** 10 # 累乗

x = 3 / 2   # 返り値＝浮動小数点
x = 3 // 2  # 返り値＝整数

x = 5 % 3   # 剰余

x++         # この書き方は使えない
x--         # この書き方は使えない


# 文字列リテラル
s = "abc'def"
s = 'abc"def'
s = r'\d+\s\n'  # raw文字列(見たままの文字として扱う)


# 文字列操作
"abcdef"[0]
"abcdef"[0] = "x" # => エラー
"abcdef"[-1]

"abcdef".title()
"abcdef".lower()
"abcdef".upper()
"abcdef".endswith('f')
"abcdef".startswith('a')
"abcdef".strip()
"abcdef".count('c')
"abcdef" + "ghijkl"
"abcdef" * 3
"abcdef".replace("abc","replaced")

"abcdef".find('x')  #=> -1
"abcdef".index('x') #=> ValueError

# 左寄せ、右寄せ、中寄せ
"abcdef".ljust(10," ")
"abcdef".rjust(10," ")
"abcdef".center(10," ")

"abc def".split(" ")
" ".join(["abc","def"])

len("abcdef")

ord("a")
chr(52)

if "a" in "abcdef":
    do_something()

# 文字列のフォーマット
"{0} {1} {0}".format("Mika", "Mike")
"{name0} {name1} {name0}".format(name0="Mika", name1="Mike")
"{:.2%}".format(6260 / 12776) # ％表記


# 値の交換(丸括弧を使わずタプルを生成)
b, a = a, b


# ヒアドキュメント
lines = '''
    このように
    複数行
    記述できます

    改行が入れたくない場合、 \
    末尾にバッククオート(\)をつけて
'''


# インデントを維持したい場合は()を使う(カンマ無し)
lines = ("aaaaaa"
  "bbbbb"
         "ccccc")


# 条件演算子(3項演算子)
return "odd" if odd(x) else "even"

s = "odd" if odd(x) else "even"


# 型変換
int("123")
hex(1023)
bin(15)
oct(7)
float("1.3")
str(123)
tuple([1,2,3])
list((1,2,3))


# 進数変換
int("0x100", 16)
int("0b1111", 2)
int("0o1777", 8)


# ビット演算
x | y   # or
x & y   # and
x ^ y   # xor
x << y  # left shift
x >> y  # right shift


# 関数
def functionname(x):
    """
    関数のコメント
    """
    do_something()
    return result


def moveTo(x,y=0):  # 引数のデフォルト値
    do_something()

moveTo(x=1, y=20)   # 引数のキーワード指定

# 条件分岐
if s == "abc":  # = ではなく ==
    statementA()
elif s == "def":
    statementB()
else:
    statementC()

if min <= value <= max: # 比較演算子を連続して書ける
    do_something()


# 複数の返り値(アンパック代入)
def foo():
    minValue = 1
    maxValue = 9
    return minValue, maxValue

minValue, maxValue = foo()

(minValue,  # 最小値
 maxValue,  # 最大値
 ) = foo()


# 可変引数
def foo(a, b, *vals):
    print(a, b, vals)

foo(1, 2, 3, 4)     # => 1, 2, (3, 4)


# 可変キーワード引数
def foo(a, b, **args):
    print(a, b, args)

foo(1, 2, c=3, d=4)     # => 1, 2, {'c': 3, 'd': 4}


# 条件演算子： == != > < <= >= not in
# 論理演算子： and or xor


# switch文はpythonにはない


# 繰り返し（指定回数）
for i in range(6): # i = 0 to 5
    do_something()


for i in range(1, 10, 2): # 開始, 終了, ステップ i= 1,3,5,7,9
    do_something()


# ループ制御

    continue
    break


# While文
while condition:
    do_something()


# python に do ～ while はない


for loopCounter, item in enumerate(seq):    # ループカウンター付き
    print(loopCounter, item)


for no, name in zip([1, 2, 3, 4], ['name1', 'name2', 'name3', 'name4']):    # 2つのシーケンスを結合
    print(no, name)


# 例外処理
try:
    if condition:
        raise Exception()   # 例外を故意に発生
except Exception as e:
    # エラー処理
    msg = "{1}(err={2})".format(e.errno, e.strerror)
    sys.stderr.write(msg)
else:
    # 例外が発生しなかった時の処理
finally:
    # 後処理（必ず実行される）

try:
    ...
except Exception as e:
    print e, 'error occurred'


# with文 : ブロックの実行を効率的に行えるようにする
#          処理に失敗した場合は、ブロックを実行しない

with open(fn) as f: # ここで失敗したらブロック内の処理は実行しない
    for line in f :
        print(line)

## tracebackモジュールで例外を取り扱う
import traceback

try:
    do_something()
except:
    traceback.print_exc()               # 例外を表示
    message = traceback.format_exc()    # 文字列として取得

# リスト
a = [1, 2, 3, 4, 5]
a[0]
a[-1]   # 負の数なら末尾から
a[5] # => Error

# スライス：取り出したい要素の最後のインデックス＋１を与える
a[1:3]      #=> a[1] ～ a[3 - 1] まで取得 => [2, 3]
a[2:]       #=> [3, 4, 5]
a[:3]       #=> [1, 2, 3]
a[2:100]    #=> [3, 4, 5]
a * 2       #=> [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
a + [6,7]   #=> [1, 2, 3, 4, 5, 6, 7]
a[1] = "x"  #=> [1, "x", 3, 4, 5, 6, 7]

del a[1]    #=> [1, 3, 4, 5, 6, 7]

a.index(1)

if 1 in a:
    do_something()

max(a)
min(a)
a.sort()    # 書き換わるので注意
a.sort(key=compareFuncName)
a.reverse() # 書き換わるので注意

a.append(6) # add() ではない
a.extend([6, 7, 8])
a.remove(1)
a.pop(0)


# 多次元配列
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix[0][2]


# タプル
# (書き換えのできないリスト / メモリ効率良 / ディクショナリのキーとして利用可)
t = (1, 2, 3, 4, 5)

# その他はリストと同じ

# 使い方の例
ipmap = {(192.168.0.1):"host1.name.com",
         (192.168.0.2):"host2.name.com",}


# ディクショナリ
dict = { "key1":"東京都", "key2":"大阪府" }
dict["key1"]

# .get():キーが無くてもエラーにならず指定値を返す
for word in lines.split():
    wordcount[word] = wordcount.get(word, 0) + 1


dict["key1"] = "北海道"
del dict["key1"]
dict.keys()
dict.values()
dict.items()    # key,valueのタプルのリストを返す

if "key1" in dict:
    do_something()


# 合成
dict1.update(dict2) # 同じキーは上書き

# set（集合）
s = {1, 2, 3, 4}
s2 = {5, 6}

s.remove(7)     # KeyError
s.discard(7)    # no error

s.add(7)
s |= {7}

if s == s2:
    do_something()

if 1 in s:
    do_something()

s.union(s2)                 # s | s2 和集合
s.intersection(s2)          # s & s2 共通集合
s.difference(s2)            # s - s2 差集合
s.symmetric_difference(s2)  # s ^ s2 対称的差集合


# map(シーケンスの各要素を変換)
map1 = map(str,  range(5))

# Null判定
if x is (not) None:
    do_something()


# ファイル読み込み
f = open("foo.txt", "r", encoding="utf-8")
s = f.read()
line = f.readline()     # 1行
lines = f.readlines()   # 全行
f.close()

# ファイル書き込み
f = open("foo.txt", "w", encoding="utf-8")
f.write(s)
f.writelines(seq)   # 改行を付加しないので注意
f.close()

# 内包表記（コンプリヘンション）
sq = [x ** 2 for x in range(5)]
sq #=> [0, 1, 4, 9, 16]

val = 10
[x for x in range(1,val) if val % x == 0]   #=> [1, 2, 5]


filter2 = [x for x in ['cat','dog', 'bird'] if 'cat' in x]
filter2 #=> ['cat']

tz = {"GMT" : "+000", "BST" : "+100",
      "EET" : "+200", "JST" : "+900"}
revtz = {value : name for name,  value in tz.items()}
revtz   #=> {'+200': 'EET', '+100': 'BST', '+000': 'GMT', '+900': 'JST'}

names = ['BOB', 'Burton', 'dave',  'bob']
unames = {x.title() for x in names}
unames  #=> {'Bob', 'Dave', 'Burton'}

# 何もしない命令

pass

# ユニットテスト

from Hoge import *  # テスト対象
import unittest

class HogeClassTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFooMethod(self):
        self.assertEqual(1, Hoge().foo())

if __name__ == "__main__":
    unittest.main()


# コード片の時間計測

import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)


# コマンドライン取得
for arg in sys.argv[1:] # argv[0]=スクリプト自身の名前
    print(arg)


# コマンドラインオプション解析
from arse import OptionParser

VERSION = '1.01'

def main():
    version = '%prog version ' + VERSION
    usage = "usage: %prog [options] directories..."
    description = 'Delete empty directories.'

    parser = OptionParser(version=version, usage=usage,
                          description=description)
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        print "reading %s..." % options.filename

if __name__ == "__main__":
    main()

# イテレータ（外部イテレータ）
# (組み込みオブジェクトはすべてイテレータに変換可能)
# (定義するためにはクラスを定義する必要があり面倒)

i = iter([1, 2, 3]) # イテレータオブジェクトに変換
next(i)             # 次の要素を取りだす(要素がなくなればStopIteration例外)

for line in open("test.txt"):   # ファイルの各行を処理
    print(line, end=" ")

# ジェネレータ（内部ジェネレータ）
# (イテレータのような機能を関数を使って定義)
# yield文を使う

def get_primes(x=2):
    while True:
        for i in range(2, x):
            if x  %  i  == 0:
                break
        else:
            yield x
        x += 1

i = get_primes()
for c in range(10):
    print(next(i))

# ジェネレータ式による生成

gen = (ord(s) for s in 'Python')
next(gen)

for code in (ord(s) for s in 'Python'):
    print(code)

# ユニットテスト

#TODO:後で書く


# ラムダ式

lambda x: x * 10


# メインで実行された時だけ実行するブロック
# (他のスクリプトからインポートされていない)

if __name__  ==  '__main__':
    do_something()


# クラス定義とインスタンス生成

class Person(SuperClassName): # クラス名は大文字
    def __init__(self, name, age): # 初期化(第1引数self必須)
        self.name, self.age = name, age
        self.address = None

bob = Person('Bob', 15)
print bob.name
bob.address = 'USA'

## クラスの継承（多重継承可）

class Person(SuperClassName):
    def __init__(self, width):
        super().__init__()  # 親クラスの呼び出しはsuper()
        self.width = width

# アトリビュート（インスタンス変数）追加の制限

class Klass:
    __slot__ = ['width', 'height']  # ここに書いてないアトリビュートは追加不可
    def __init__(self):
        self.width = 0
        self.height = 0

i = Klass()
i.width = 1
i.c = 0 # AttributeError

# メソッドやアトリビュートの隠蔽（カプセル化） 名称の頭に＿をつける
self._size # クラス外部からアクセス不可になる
self.__size # クラス外部からアクセス不可になる

## Setter / Getter(データを変更もしくは参照する専用のメソッド)
## プロパティ(Setter / Getterを手軽に定義するための機能）
## アトリビュートのようにクラスの外側から好き勝手書き換えられないようにする

class Prop(object):
    def __init__(self):
        # 内部で使うのはプロパティ名xとは違う名前(無限ループ防止)
        self.__x = 0

    def getx(self):     # Getter
        return self.__x

    def setx(self, x):  # Setter
        self.__x = x

    # プロパティxのgetter, Setterを設定
    x = property(getx, setx)

i = Prop()
i.x = 0


## 演算子のオーラーライド(再定義)

__add__(self, other)        # + (self + other)
__sub__(self, other)        # -
__mul__(self, other)        # *
__truediv__(self, other)    # /
__floordiv__(self, other)   # //

__iadd__(self, other)       # +=
__isub__(self, other)       # -=
__imul__(self, other)       # *=
__itruediv__(self, other)   # /=
__ifloordiv__(self, other)  # //=

__or__(self, other)         # | (or)
__and__(self, other)        # & (and)

## 比較演算子のオーラーライド
## equal, not equal, lesser than, greater than, ...

__eq__(self, other)         # ==
__ne__(self, other)         # !=
__lt__(self, other)         # <  (self < other)
__gt__(self, other)         # >

__le__(self, other)         # <=
__ge__(self, other)         # >=

## 型変換のオーバーライド

__int__(self)   # int()
__bytes__(self)
__float__(self)
__str__(self)
__repr__(self)  # 印字可能な文字列表現に変換

__format__(self, form_spec) # format()でのフォーマットの再定義

## コンテナ型で利用する特殊メソッド

__len__(self)   # len()
__getitem__(self, key) # obj[key]
__setitem__(self, key, value) # obj[key] = value
__delitem__(self, key) # del obj[key]

__iter__(self)  # iter() : イテレータオブジェクトを返す
                # (内部で__next_()というメソッドを定義する必要あり)

__getattr__(self, attributeName)    # オブジェクトに存在しない
                                    # アトリビュートが参照されるときに呼ばれる
                                    # 属性が存在しないことにしたければ
                                    # raise AttributeError
__getattrubute__(self, attributeName)    # 無条件で呼ばれる__getattr__

__setattr__(self, attributeName, value)  # 代入するときに呼び出される

__call__(self[, args...])   # オブジェクトの名前に続いて丸括弧が添えられ
                            # 関数として呼びだされた時に呼ばれる

__del__(self)   # デストラクタ

__hash__(self)  # hash() ハッシュ値を整数で返す

## オブジェクトの型判定

isinstance(var, type)   # 型判定(ype= str, int, float, ...)

## アトリビュート（メソッド含む）の取得
s = "abcde"

s.find("cd")
getattr(s, "find")("cd") # find()メソッドを呼び出す


# 標準ライブラリ

## Webサーバからデータを取得
from urllib import request
src = request.urlopen('http://www.python.org/').read()

from urllib import request,  parse
url = 'http://www.python.org/somefile.zip'
filename = parse.urlparse(url)[2].split('/')[-1]
request.urlretrieve(url, filename)

## 順番付きディクショナリ
from collections import OrderedDict
od = OrderedDict()

## デフォルト値付きディクショナリ
from collections import defaultdict
animals = [('猫', 'メインクーン'),
           ('猫', 'アビシニアン'),
           ('犬', 'パグ'),
           ('犬', 'シベリアンハスキー'),
           ('犬', 'ブルドッグ') ]
dd = defaultdict(list) # 空のリストを初期値に持つディクショナリ
for k, v in animals :
    dd[k].append(v)

dd # =>  defaultdict(<class 'list'>, {'猫': ['メインクーン', 'アビシニアン'], '犬': ['パグ', 'シベリアンハスキー', 'ブルドッグ']})


## ソート済みのリストへ要素を追加する支援
import bisect

## 日時を取り扱う
import datetime

datetime.date.today()   # 今日
datetime.datetime.now() # 現在の日時

datetime.datetime(2014, 3, 2, 16, 32, 00)
datetime.time(16, 32, 00)
datetime.date(2014, 3, 2)

d = datetime.date(2014, 3, 2)
d.year  #2014
d.month # 3
d.day # 2
d.weekday() # 6:日用日
d.strftime('%Y/%m/%d %H:%M:%S') # '2014/03/02 00:00:00'

d = datetime.strptime('2014/03/02 00:00:00', '%Y/%m/%d %H:%M:%S')

### 日時の差(比較や乗除算も可能)
delta = datetime.timedelta(days=5)
d1 = datetime.date(2014, 2, 6)
d2 = d1 + delta
print(d2)   # 2014-02-11

d2 = datetime.date(2014, 3, 2)
d1 = datetime.date(2014, 2, 6)
d2 = datetime.date(2014, 3, 2)
delta = d2  -  d1
print(delta)    # 24 days, 0:00:00

## カレンダーに関する情報を取得
import calendar

### 指定年月の曜日と日数
(days, first_weekday) = calendar.monthrange(2014, 2)
print(days, first_weekday) #5 28

calendar.month(2014, 2) # カレンダーを出力

## 正規表現
import re

re.findall(r'[abcde]', 'abcdefg')   # ['a', 'b', 'c', 'd', 'e']
re.split(r',', 'ab,cde,fg')         # ['ab', 'cde', 'fg']
re.sub(r'a', 'b', 'abcde')          # 'bbcde'

match = re.search(r'a', 'abcdea')
print(match)
match = re.match(r'a', 'abcdea')
print(match)

for match in re.finditer(r'[a-z]+', 'This is a pen.'):
    print(match.group(0), end =' ') # his is a pen

s = 'abcd,efgh,ijkl'
r = re.compile(r'[abcde]', re.IGNORECASE | re.MULTILINE  | re.DOTALL)
r.findall(s)

## システムパラメータを取得・操作
import sys

sys.argv[0]  # 実行中のスクリプト自身
sys.argv[1:] # コマンドラインパラメータ
sys.exit(0)
sys.getdefaultencoding()

## ファイルシステム・プロセス等のOS依存の情報を取得・操作
import os

os.getenv(key, default=None)
os.chdir(path)
os.getcwd()
os.remove(path)
os.rename(src, dest)
os.mkdir(path, mode)
os.mkdirs(path, mode)   # 途中のパスも作成
os.rmdir(path)
os.removedirs(path) # 途中も削除

os.path.exists(path)
os.path.getsize(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.join(path, path2, ...)
dirname, filename = os.path.split(path)

path = r'c:\users\default\desktop.ini'
os.path.dirname(path)   # ディレクトリ名
os.path.basename(path)  # ファイル名
path_without_ext, ext = os.path.splitext(path) # 拡張子


## 数学モジュール
import math

math.pi
mati.sqrt(2)
mati.sin(60)
mati.cos(60)
mati.tan(60)

## 乱数
import random

random.seed(value) # 乱数の種

x = random.random() # 0 <= x <= 1
y = random.randint(1, 10) # 1～10 の整数

### 階層を渡り歩く
for dirpath, dirnames, filenames in os.walk(path, topdown=True, oneerror=None):
    do_something()

### プロセス / 外部コマンドの実行
exit_status = os.system(command)   # プロセス実行し終了まで待つ(終了コードを返す)
os.startfile(path)  # WindowsのStartコマンド

import commands
stdout_text = commands.getoutput(command)   # プロセス実行し終了まで待つ(標準出力を返す)