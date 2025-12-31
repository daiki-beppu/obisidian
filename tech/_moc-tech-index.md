---
title: Tech Notes Master Index
type: moc
created: 2025-12-31
tags: [moc, index]
---

# Tech Notes マスターインデックス

## 🗂️ 学習パス

### メインシリーズ
- [[_moc-react-nextjs-learning]] - React & Next.js 学習パス (17記事)
- [[_moc-typescript-learning]] - TypeScript 学習パス (10記事)

### サポートコンテンツ
- [[_moc-devtools]] - 開発ツール・環境構築 (8記事)

---

## 📊 全体進捗サマリー

```dataview
TABLE
  series AS "シリーズ",
  length(rows) AS "記事数",
  length(filter(rows, (r) => r.status = "completed")) AS "完了",
  round(length(filter(rows, (r) => r.status = "completed")) / length(rows) * 100) + "%" AS "進捗率"
FROM "tech"
WHERE series != null
GROUP BY series
```

---

## 🏷️ トピック別ビュー

### フロントエンド
- [[_moc-react-nextjs-learning]] - React/Next.js

### 言語
- [[_moc-typescript-learning]] - TypeScript

### 開発環境
- [[_moc-devtools]] - ツール全般

### その他
- [[seminar-corporate-finance]] - セミナー
- [[technical-debt-early-detection-guide]] - 技術的負債
- [[devin-utilizing]] - AI活用
- [[news-share]] - ニュース
- [[lessons-from-discussion]] - ディスカッション

---

## 📈 タグクラウド

```dataview
TABLE WITHOUT ID
  tag AS "タグ",
  length(rows) AS "記事数"
FROM "tech"
FLATTEN file.tags AS tag
WHERE tag != null
GROUP BY tag
SORT length(rows) DESC
LIMIT 20
```

---

## 📅 最近の学習

```dataview
TABLE
  title AS "タイトル",
  topic AS "トピック",
  updated AS "更新日"
FROM "tech"
WHERE type != "moc"
SORT updated DESC
LIMIT 10
```

---

## 🎯 学習ロードマップ

### 現在のフォーカス
1. React/Next.js Phase 5の完了
2. TypeScript Phase 3-4の進行

### 次の学習候補
- [ ] Next.js App Router
- [ ] React Server Components
- [ ] TypeScript 高度な型
- [ ] テスト（Jest/React Testing Library）
