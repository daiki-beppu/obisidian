---
source: "https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/hhfj3/prompts-%26-summaries-of-lessons"
published: 2025-08-06
created: 2026-01-04
---
#データ

#ClaudeCode #DeepLearningAI #学習ガイド

## プロンプトとレッスンの要約 (Claude Code)

### プロンプト
各レッスン（L2〜L8）のプロンプトとノートへのGitHubリンクが提供されています。

### 追加リソース
Claude Codeの公式ドキュメント、共通ワークフロー、ベストプラクティス、ユースケース、Anthropic Academyの「Claude Code in Action」コースが紹介されています。

### Claude Code機能の概要

#### プロジェクトメモリの管理
*   **`/init`**: コードベースをスキャンし、`CLAUDE.md`ファイルを生成。これはClaude Codeへのガイドとなり、常にコンテキストに含まれる。
*   **`#`**: 迅速にメモリを追加。例：`#use uv to run python files`、データベーススキーマの記述。

#### Claude Codeコマンドの概要
| コマンド | 説明 |
| :------ | :--- |
| `/clear` | 現在の会話履歴をクリア |
| `/compact` | 現在の会話履歴を要約 |
| `ESC` | Claudeを中断し、方向転換または修正 |
| `ESC ESC` | 会話を以前の時点に戻す |
| `@` | ファイルをメンションし、その内容をリクエストに含める |
| `/mcp` | MCP接続の管理と利用可能なMCPサーバーの確認 |
| `!` | 通常のbashコマンドを実行（例: `!pwd`） |
| `exit` | Claude Codeを終了 |

#### ショートカット
*   `shift+tab`: プランニングモードと自動承認モードを切り替える。
*   スクリーンショット: `cmd+shift+ctrl+4` (Mac) または `Win + Shift + S` (Windows)。
*   スクリーンショットの貼り付け: `Ctrl + V`。

#### 追加のClaude機能
*   **Extended Thinking Mode**: 複雑なタスク（例: 複雑なアーキテクチャ変更、デバッグ）には「think」, 「think hard」, 「think harder」, 「ultrathink」を使用してClaudeの思考バジェットを増やす。
*   **サブエージェントの使用**: Claude Codeは「Task」ツールを用いてサブエージェントを起動可能。ブレインストーミングや問題の多角的な調査に明示的にサブエージェントの使用を依頼できる。カスタムサブエージェントの作成も可能（本コースでは扱わず）。