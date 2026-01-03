---
title: 01-react-with-nextjs-17
created: 2025-01-21
updated: 2025-01-21
topic: 01
subtopics: []
tags: ['01']
status: completed
difficulty: beginner
prev: null
next: null
related: []
---

## 💡 学んだことの要約

## 📝 詳細

### 背景

### 内容

fetcher 関数をモジュールとして切り出し

<details>
<summary>サンプルコード(クリックで開く)</summary>

```jsx
// /src/utils/fetcher.js

export const fetcher = async (url) => {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error('エラーが発生しました');
  }

  const json = await response.json();

  return json;
};
```

あとは fetcher をインポートするだけ！

</details>

### ハマったポイント

## 🔍 気づき・感想

## 📚 参考リンク

## ⏭️ 次に学びたいこと

## 📌 関連する過去の学び

---

## 🔗 このシリーズの学習パス

← 前: [[react-nextjs-16-swr-chaining]]
→ 次: なし

**シリーズ全体**: [[_moc-react-nextjs-learning]]
