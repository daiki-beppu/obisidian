---
source: "https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously"
published: 2025-08-06
created: 2026-01-04
---
#データ


# Claude Code と Git Worktrees

### カスタムコマンドの作成
*   `.claude/commands` フォルダ内にMarkdownファイルを作成して定義する。
*   `$ARGUMENTS` 変数を使用してコマンド引数を参照可能。
*   カスタムコマンドは `CLAUDE.md` と異なり、特定の会話でのみ使用される。

### Git Worktrees を使った並行開発
*   **目的:** 複数のClaude Codeセッションで同じファイルを上書きせずに並行して機能開発を行う。
*   **手順:** `git worktree add` コマンドで `.trees` フォルダ内に複数の独立したワークツリーを作成する。
*   各ワークツリーで異なる機能（例: UI、テスト、コード品質）を並行して実装。

### マージと競合の解決
*   各ワークツリーでの作業完了後、変更をコミットする。
*   メインブランチに戻り、Claude Code に `git merge` コマンドでワークツリーをマージさせる。
*   Claude Code はマージ競合を分析し、自動的に解決・コミットを支援できる。


#ClaudeCode  #学習ガイド #開発効率