---
title: react-with-nextjs-11
created: 2025-01-15
updated: 2025-01-15
series: React & Next.js Learning Path
sequence: 12
topic: react
subtopics: []
tags: ['react', 'nextjs', 'beginner']
status: completed
difficulty: beginner
prev: null
next: null
related: []
---

### 内容

非同期処理のエラーとローディングについて

`chrome dev tools` の `Network` タブ のなかの `throttling` で
回線の速度を調整することができる

custom から自身で速度を設定する事もできる

エラーとローディングの処理方法

<details>
<summary>サンプルコード(クリックで開く)</summary>

```jsx
import { useCallback, useEffect, useState } from 'react';

const Posts = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchPosts = useCallback(async () => {
    try {
      const response = await fetch(
        'https://jsonplaceholder.typicode.com/posts'
      );

      if (!response.ok) {
        throw new Error('エラーが発生しました');
      }

      const json = await response.json();
      setPosts(json);
    } catch (error) {
      setError(error);
    }
    setLoading(false);
  }, []);

  useEffect(() => {
    fetchPosts();
  }, [fetchPosts]);

  if (loading) {
    return <div>ローディング中</div>;
  }

  if (error) {
    return <div>{error.massage}</div>;
  }

  if (posts.length === 0) {
    return <div>データは空です</div>;
  }

  return (
    <ol>
      {posts.map((post) => {
        return <li key={post.id}>{post.title}</li>;
      })}
    </ol>
  );
};

export default Posts;
```

</details>

### ハマったポイント

## 🔍 気づき・感想

非同期処理のエラーやローディングについては
現状は古い記述方法にはなるが仕事で使っているのでちょうど良かった

## 📚 参考リンク

## ⏭️ 次に学びたいこと

## 📌 関連する過去の学び

---

## 🔗 このシリーズの学習パス

← 前: [[react-nextjs-10-api-fetching]]
→ 次: [[react-nextjs-12-usereducer]]

**シリーズ全体**: [[_moc-react-nextjs-learning]]
