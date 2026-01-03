---
title: react-with-nextjs-10
created: 2025-01-13
updated: 2025-01-13
series: React & Next.js Learning Path
sequence: 11
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

API の叩き方

外部のライブラリを使用せず自力で書く

<details>
<summary>サンプルコード(クリックで開く)</summary>

```jsx
import { useCallback, useEffect, useState } from 'react';
import { Header } from 'src/components/Header';

const Home = () => {
  const [posts, setPosts] = useState([]);

  const fetchPosts = useCallback(async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    const json = await response.json();
    setPosts(json);
  }, []);

  useEffect(() => {
    fetchPosts();
  }, [fetchPosts]);
  return (
    <>
      <Header />
      {posts.length > 0 ? (
        <ol>
          {posts.map((post) => {
            return <li key={post.id}>{post.title}</li>;
          })}
        </ol>
      ) : null}
    </>
  );
};

export default Home;
```

</details>

## 🔍 気づき・感想

超基本的な API の叩き方を理解できた！

今後は少し踏み込んで、ローディングやエラーハンドリングについて学習しようと思う

## 📚 参考リンク

## ⏭️ 次に学びたいこと

## 📌 関連する過去の学び

---

## 🔗 このシリーズの学習パス

← 前: [[react-nextjs-09-usememo-router]]
→ 次: [[react-nextjs-11-error-loading]]

**シリーズ全体**: [[_moc-react-nextjs-learning]]
