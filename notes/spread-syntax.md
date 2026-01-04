---
title: spread-syntax
created: 2026-01-04
updated: 2026-01-04
---

#log #output

# スプレッド構文について

スプレッド構文とは配列やオブジェクトなどの列挙可能なオブジェクトを展開するときに使う
展開したい列挙可能なオブジェクトの前に `...` を記述する

```JavaScript

記述例

// 配列のコピーを作成
const array = [1, 2, 3, 4];

console.log(...array);
// 1 2 3 4

// 配列を展開した値を配列に入れている
const newArray = [...array];

console.log(newArray);
// [ 1, 2, 3, 4 ]

// concatを使わない配列の連結
const numArray = [1, 2, 3, 4];
const strArray = ["one", "two", "three", "four"];

const newArray = [...numArray, ...strArray];
console.log(newArray);
// [ 1, 2, 3, 4, 'one', 'two', 'three', 'four' ]

```

オブジェクトの要素を複製するときにも使える

```JavaScript

記述例

// オブジェクトの要素を複製
const lastYearProfile = {
  name: "daiki",
  birthday: "12月28日",
  skills: ["HTML", "CSS",],
};

const twoYearAgoProfile = {
  name: "daiki",
  birthday: "12月28日",
  skills: ["HTML5", "CSS3", "JavaScript", "Ruby"],
  target: "webエンジニア",
};

const currentProfile = {
  ...lastYearProfile,
  ...twoYearAgoProfile,
};

console.log(currentProfile);
/*
{
  name: 'daiki',
  birthday: '12月28日',
  skills: [ 'HTML', 'CSS', 'JavaScript', 'Ruby' ],
  target: 'webエンジニア'
}
*/


```

> [!TIP]
> 破壊的メソッド:`push` `pop` などを
> 使いたくない場合などにも使用する

## レスト構文について

レスト構文とは引数をまとめて渡すための構文

> [!WARNING]
> スプレッド構文と同じ記述に見えるが逆の動きをするので注意！

### argument オブジェクト

アロー関数以外のすべての関数で使える配列のようなオブジェクト
厳密には配列ではなく `push` や `pop` は使えないただ `length` は使える
argument オブジェクトには関数に渡された引数がすべて入っている

```JavaScript

記述例

function strLength() {
  console.log(arguments);
}

strLength();
// [Arguments] {}

strLength("cat", "にゃんこ", "ぬこ様");
// [Arguments] { '0': 'cat', '1': 'にゃんこ', '2': 'ぬこ様' }

// 文字列の長さが最大の値を返す関数
function maxStrLength() {
  return arguments.reduce((maxStr, str) => {
    if (str.length < maxStr.length) {
      return maxStr;
    } else {
      return str;
    }
  });
}

maxStrLength("cat", "にゃんこ", "ぬこ様");
// TypeError: arguments.reduce is not a function
// argumentsは配列ではないためエラーになる


```

こういったときにレスト構文が使える

```JavaScript

記述例

// 文字列の長さが最大の値を返す関数
function maxStrLength(...words) {
  return words.reduce((maxStr, str) => {
    if (str.length < maxStr.length) {
      return maxStr;
    } else {
      return str;
    }
  });
}

※ ...wordsのを...を忘れないように！

console.log(maxStrLength("cat", "にゃんこ", "ぬこ様"));
// にゃんこ

```

## 🔗 関連トピック

**基礎知識**:
- [[array-overview]] - 配列の展開とコピー
- [[object-overview]] - オブジェクトの展開とマージ

**実践で使う**:
- [[react-nextjs-06-immutability]] - Reactでのイミュータビリティ
- [[react-nextjs-01-components-basics]] - propsの展開

---
