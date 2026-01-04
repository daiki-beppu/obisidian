---
title: object-overview
created: 2026-01-04
updated: 2026-01-04
---

#log #output

# オブジェクトについて

JavaScript でいうオブジェクトとは
他のプログラミング言語でいうところの｢連想配列｣のこと

## オブジェクトの作り方

オブジェクトリテラルを使ってつくることができる
オブジェクトリテラルとは`{}(ブレース)`を用いて記述する

```JavaScript

記述例

const profile {
  name: daiki,
  age : 27,
  bio : "december,28"
  // オブジェクトに配列も入れられる
  skills: ["HTML", "CSS", "JavaScript"]
  // オブジェクトを入れることもできる
  obj: {
    foo: "bar"
    hoge: "huga"
    fiz: "buz"
  }
}

```

## オブジェクトの取り出し方

オブジェクトの取り出し方は 2 通り

`.(ドット)`を用いる方法と`[]ブラケット`を用いる方法

```JavaScript

記述例

const profile = {
  name: "daiki",
  age: 27,
  bio: "december,28",
  skills: ["HTML", "CSS", "JavaScript"],
  obj: {
    foo: "bar",
    hoge: "huga",
    fiz: "buz",
  },
};

// .(ドット)を用いる方法
console.log(profile.skills);

// [](ブラケット)を用いる方法
console.log(profile["skills"]);
// [ 'HTML', 'CSS', 'JavaScript' ]

```

`[]`(ブラケット)を用いる場合は String と変数を区別するため
必ずどちらかわかるように記述しないといけない

```JavaScript

記述例

const profile = {
  name: "daiki",
  age: 27,
};

console.log(profile[age]);
// エラー ReferenceError: age is not defined

```

## オブジェクトの更新

```JavaScript

const profile = {
  firstName: "daiki",
  lastName: "beppu",
  age: 27,
  birthday: "december,28",
};

// オブジェクトの要素を追加
profile.job = "engineer";
console.log(profile);
/* {
  firstName: 'daiki',
  lastName: 'beppu',
  age: 27,
  birthday: 'december,28',
  job: 'engineer'
}
*/

// オブジェクトの要素を更新
profile.age = 28;
console.log(profile);
/* {
  firstName: 'daiki',
  lastName: 'beppu',
  age: 28,
  birthday: 'december,28'
} */
```

## 🔗 関連トピック

**基礎知識**:
- [[variable-overview]] - オブジェクトも変数で扱う
- [[array-overview]] - 配列とオブジェクトの関係

**モダン構文**:
- [[destructuring-assignment]] - オブジェクトの分割代入
- [[spread-syntax]] - オブジェクトの展開とマージ

**実践で使う**:
- [[react-nextjs-01-components-basics]] - propsはオブジェクト
- [[typescript-06-object-types]] - オブジェクトの型定義

---
