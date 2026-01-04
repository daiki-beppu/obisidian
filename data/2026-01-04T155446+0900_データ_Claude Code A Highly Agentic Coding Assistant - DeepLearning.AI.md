---
source: "https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/nngi6/exploring-github-integration-%26-hooks"
published: 2025-08-06
created: 2026-01-04
---
#データ



## 💻 Claude Code の GitHub 連携とフック機能
### GitHub 連携の導入
-   **目的**: ターミナル外で Claude Code を利用し、GitHub のプルリクエストレビューや課題修正を自動化する。
-   **インストール**: `/install-GitHub-app` コマンドを使用し、ブラウザで GitHub アプリをインストール。
-   **ワークフロー設定**: 
    -   GitHub Issues で Claude をタグ付けして使用。
    -   Pull Requests でコードを自動レビュー。
    -   これにより、バグ修正、テスト作成、コードレビューが GitHub Actions 経由で可能になる。
-   **コードレビュー**: Claude は PR が開かれると自動でコードを分析し、品質、セキュリティ、その他の考慮事項について詳細な評価を提供する。
-   **課題修正**: GitHub Issue で Claude をタグ付け（例: `Claude, can you fix this for me?`）すると、Claude が問題を分析し、計画を立て、修正し、プルリクエストを生成する。Claude 自身が作成したコードをレビューすることも可能。

### Claude Code のフック機能
-   **概要**: Claude Code の操作ライフサイクル（ツールの実行前/後、通知送信時など）の任意の時点で特定のコードを挿入できる機能。
-   **設定**: `/hooks` コマンドで設定を管理。設定は `.claude/settings.local.json` に保存される。
-   **イベントの種類**: 
    -   Before/PostToolUse (ツール実行前/後)
    -   NotificationSent (通知送信時)
    -   UserPrompt (ユーザーがプロンプト送信時)
    -   Stop (停止時)
    -   BeforeSubagentConclusion (サブエージェントが応答を終了する前)
-   **例**: `PostToolUse` フックで `Read` または `Grep` ツールが使用された後に `say 'All done!'` コマンドを実行する。
-   **応用**: テストの実行、リンターの実行、不必要なツールの使用停止、特定のイベント発生時の Claude 自身のレビューなど。

#DeepLearningAI, #ClaudeCode, #GitHub連携