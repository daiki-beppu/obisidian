---
title: React & Next.js Learning Path
type: moc
topic: react
created: 2025-01-01
tags: [moc, react, nextjs, learning-path]
---

# React & Next.js 学習パス

## 📊 学習進捗

- [x] **Phase 1: 基礎** (1-3) - 完了
- [x] **Phase 2: Hooks & State** (4-6) - 完了
- [x] **Phase 3: 応用パターン** (7-9) - 完了
- [x] **Phase 4: 非同期 & API** (10-13) - 完了
- [ ] **Phase 5: 発展** (14-17) - 進行中

全体進捗: 13/17 (76%)

---

## 📚 学習フロー（推奨順序）

### Phase 1: 基礎（1-3）
1. [[react-nextjs-01-components-basics]] - コンポーネント・Props・Children
2. [[react-nextjs-02-link-routing]] - ルーティング・Link
3. [[react-nextjs-03-css-modules]] - CSS Modules・スタイリング

### Phase 2: Hooks & State（4-6）
4. [[react-nextjs-04-lifecycle-state]] - useEffect・useState
5. [[react-nextjs-05-hooks-dependencies]] - 依存配列・クリーンアップ
6. [[react-nextjs-06-immutability]] - イミュータビリティ・配列操作

### Phase 3: 応用パターン（7-9）
7. [[react-nextjs-07-custom-hooks]] - カスタムフックス
8. [[react-nextjs-08-state-lifting]] - Stateリフトアップ
9. [[react-nextjs-09-usememo-router]] - useMemo・useRouter

### Phase 4: 非同期 & API（10-13）
10. [[react-nextjs-10-api-fetching]] - API基礎
11. [[react-nextjs-11-error-loading]] - エラーハンドリング
12. [[react-nextjs-12-usereducer]] - useReducer
13. [[react-nextjs-13-swr]] - SWR・データフェッチング

### Phase 5: 発展（14-17）
14. [[react-nextjs-14-file-routing]] - ファイルシステムルーティング
15. [[react-nextjs-15-dynamic-routing]] - 動的ルーティング
16. [[react-nextjs-16-swr-chaining]] - SWR連続fetch
17. [[react-nextjs-17-fetcher-module]] - fetcherモジュール化

---

## 🏷️ トピック別インデックス

### コンポーネント
- [[react-nextjs-01-components-basics]] - 基礎
- [[react-nextjs-02-link-routing]] - Link
- [[react-nextjs-03-css-modules]] - スタイリング

### Hooks
- [[react-nextjs-04-lifecycle-state]] - useState・useEffect
- [[react-nextjs-05-hooks-dependencies]] - 依存配列
- [[react-nextjs-07-custom-hooks]] - カスタムフックス
- [[react-nextjs-09-usememo-router]] - useMemo
- [[react-nextjs-12-usereducer]] - useReducer

### State管理
- [[react-nextjs-04-lifecycle-state]] - State基礎
- [[react-nextjs-06-immutability]] - イミュータブル更新
- [[react-nextjs-08-state-lifting]] - リフトアップ
- [[react-nextjs-12-usereducer]] - 複雑なState

### 非同期・API
- [[react-nextjs-10-api-fetching]] - fetch基礎
- [[react-nextjs-11-error-loading]] - エラー・ローディング
- [[react-nextjs-13-swr]] - SWR
- [[react-nextjs-16-swr-chaining]] - SWR連続fetch
- [[react-nextjs-17-fetcher-module]] - fetcherモジュール化

### Pages Router
- [[react-nextjs-02-link-routing]] - ルーティング
- [[react-nextjs-03-css-modules]] - _app.js
- [[react-nextjs-09-usememo-router]] - useRouter
- [[react-nextjs-14-file-routing]] - ファイルシステムルーティング
- [[react-nextjs-15-dynamic-routing]] - 動的ルーティング

---

## 🔗 関連する学習パス

### TypeScript との組み合わせ
- [[_moc-typescript-learning]] - TypeScript学習パス
- [[typescript-01-setup-basics]] - 環境構築
- [[typescript-05-array-tuple-any]] - Reactで使う型
- [[typescript-08-alias-interface]] - Props型定義

### 開発環境
- [[_moc-devtools]] - 開発ツール全般
- [[eslint-01-flat-config-setup]] - コード品質
- [[devtools-prettier-setup]] - フォーマット

---

## 📈 学習メトリクス

```dataview
TABLE
  sequence AS "No.",
  difficulty AS "難易度",
  status AS "状態",
  created AS "作成日"
FROM "tech"
WHERE series = "React & Next.js Learning Path"
SORT sequence ASC
```

## 🎯 次の学習目標

- [ ] App Routerへの移行を学ぶ
- [ ] Server Componentsの理解
- [ ] TypeScriptとの統合強化
