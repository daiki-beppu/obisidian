---
title: typescript-01
created: 2025-01-22
updated: 2025-01-22
series: TypeScript Learning Path
sequence: 1
topic: typescript
subtopics: []
tags: ['beginner', 'typescript']
status: completed
difficulty: beginner
prev: null
next: null
related: []
---

## 💡 学んだことの要約

## 📝 詳細

### 背景

React の基礎はある程度学んだので次は `TypeScript` を学んでいく
仕事でももちろん使っているし `TypeScript` の理解を深めてもいいのではないかと言われたのもある

### 内容

なぜ `TypeScript` が必要なのか？

型を明示的に記述することで

- バグが発生しにくいコードになる
- エディターの補完が強力なものになる
- ホバーすることでドキュメント的な役割も果たしてくれる

`TypeScript` を実際に使えるようにする設定について

設定が必要な理由
ブラウザ側では `TypeScript` を実行するための環境がない
なので `TypeScript` を `JavaScript` に変換する必要がある

まずは `TypeScript` をインストールする

```shell
yarn add -D typescript

-- -D は --dev と同じ
-- devDependencies に追加するという意味
```

`tsconfig.json` を作成する

```shell
./node_modules/.bin/tsc --init

```

`.ts` ファイルをコンパイルする

```shell
./node_modules/.bin/tsc ファイル名

```

次は `Next.js` で `TypeScript` を用いた開発の準備

```shell
yarn create next-app --typescript
```

### ハマったポイント

## 🔍 気づき・感想

React, Next.js が一段落して
いよいよ本格的に TypeScript を学ぶ事ができる！

## 📚 参考リンク

## ⏭️ 次に学びたいこと

## 📌 関連する過去の学び

## 🔗 関連トピック

**React での活用**:
- [[react-nextjs-01-components-basics]] - ReactでTypeScriptを使う
- [[react-nextjs-04-lifecycle-state]] - Hooksの型付け

**開発環境の整備**:
- [[eslint-01-flat-config-setup]] - TypeScript用ESLint設定
- [[devtools-prettier-setup]] - TypeScriptのフォーマット

---

## 🔗 このシリーズの学習パス

← 前: なし
→ 次: [[typescript-02-type-annotation]]

**シリーズ全体**: [[_moc-typescript-learning]]
