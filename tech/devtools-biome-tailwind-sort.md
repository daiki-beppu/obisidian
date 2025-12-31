---
title: biome
created: 2025-04-12
updated: 2025-04-12
topic: biome
subtopics: []
tags: ['biome']
status: completed
difficulty: beginner
prev: null
next: null
related: []
---

# VSCode で Biome 使って保存時にクラス名を自動で並び替え変える方法

Biome でも `eslint-plugin-tailwindcss`のように
自動でクラス名を並び替える方法がないか調べていたところ

Biome の PR に可能な方法があったのを見つけた

```
重要な注意事項重要な注意事項と題されたセクション
このルールは進行中であり、部分的にしか実装されていません。進捗は以下の GitHub issue で追跡しています: https://github.com/biomejs/biome/issues/1274

現在のところ、ユーティリティクラスの並べ替えはフォーマッターの一部ではなく、代わりにリンタールールとして実装されています。この修正は、現段階では安全ではありません。これは、「保存時に修正」のような IDE アクションの一部として自動的に適用されないことを意味します。

このルールに関するフィードバックをお待ちしています。

問題を報告する前に、このドキュメントページ全体をお読みください。

特に、以下の機能はまだサポートされていないことを覚えておいてください：

スクリーンバリアントのソート (例: md:, max-lg:)。静的、動的、任意の variant のみがサポートされています。
カスタムユーティリティとバリアント (Tailwind CSS プラグインによって導入されたものなど)。デフォルトの Tailwind CSS 設定のみがサポートされます。
プレフィックスやセパレータなどのオプション。
オブジェクトプロパティ（clsx呼び出しなど）。
これらの機能に関する問題を報告しないでください。
```

## VSCode で Biome 使って保存時にクラス名を自動で並び替え変える方法

こちらを参考にしました

[biomejs/biome PR feat(linter): implement class sorting rule (first pass) #1362](https://github.com/biomejs/biome/pull/1362#issuecomment-2463860207)

linter の rules にこちらを追加

```json
"nursery": {
	"useSortedClasses": {
		"level": "error",
		"fix": "safe",
		"options": {
		"attributes": ["className"],
		"functions": ["cn"]
		}
	}
}
```

```json
{
	"$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
	"vcs": {
		"enabled": true,
		"clientKind": "git",
		"useIgnoreFile": true
	},
	"files": {
		"ignoreUnknown": true,
		"ignore": ["node_modules", ".next/**/*", "public"]
	},
	"organizeImports": {
		"enabled": true
	},
	"linter": {
		"enabled": true,
		"rules": {
			"recommended": true,
			"nursery": {
				"useSortedClasses": {
					"level": "error",
					"fix": "safe",
					"options": {
						"attributes": ["className"],
						"functions": ["cn"]
					}
				}
			}
		},
		"ignore": ["node_modules", ".next/**/*", "public"],
		"include": ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]
	}
}
```

useSortedClasses はデフォルトでは unsafe なので
ci から --unsafe を実行しないと修正できません

ですが biome.config でこちらの設定も変更できるみたいです。


[useSortedClasses](https://biomejs.dev/linter/rules/use-sorted-classes/)

## 📚 参考リンク

公式ドキュメント: https://biomejs.dev/

GitHub: https://github.com/biomejs/biome


