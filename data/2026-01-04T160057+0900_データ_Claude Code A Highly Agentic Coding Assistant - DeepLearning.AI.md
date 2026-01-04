---
source: "https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/vvq28/creating-web-app-based-on-a-figma-mockup"
published: 2025-08-06
created: 2026-01-04
---
#データ

### Claude CodeによるFigmaモックアップからのWebアプリ開発

このレッスンでは、Claude Codeを活用してFigmaモックアップからWebアプリケーションを迅速に開発し、Playwrightでテストする方法を学びます。

#### 主要なステップと機能

*   **環境設定**
    *   **Figma MCPサーバーとの接続**: Figmaアカウントと開発者モードを有効にし、FigmaモックアップのレイヤーをコピーしてClaude Codeに読み込ませます。
    *   **Playwright MCPサーバーの追加**: プログラムによるテストとUIの視覚的検証のためにPlaywright MCPサーバーを設定します。
    *   **Next.jsアプリケーションの初期化**: 最新バージョンのNext.jsプロジェクトを作成し、必要な依存関係をインストールします。
    *   **Claude Codeの設定**: `/mcp` コマンドで両MCPサーバーが正しく接続されていることを確認します。

*   **FigmaモックアップからのUI生成**
    *   **プロンプトによる指示**: Claude CodeにFigmaモックアップの分析、Rechartsライブラリを使用したチャート生成、PlaywrightでのUI確認を指示します。
    *   **Figmaツールの活用**: Claude CodeはFigma dev MCPサーバーの `Get image` および `Get Code` ツールを使用して、モックアップの視覚情報と基になるコードを取得します。
    *   **Next.jsでの実装**: 取得した情報に基づき、Claude CodeがNext.jsのアプリケーション構造（CSS、メタデータ、ダッシュボードレイアウト、Reactコンポーネント）を構築します。
    *   **Playwrightによる初期検証**: Claude CodeはPlaywrightを使用して `localhost:3000` にアクセスし、スクリーンショットを撮影して生成されたUIがモックアップと一致しているかを確認します。

*   **実データとの統合**
    *   **APIからのデータ取得**: Claude CodeにFederal Reserve Economic Data APIからの実データでチャートを更新するよう指示します。
    *   **Web検索とAPIキー**: Claude CodeはWeb検索ツールを使用してAPIドキュメントを調査し、APIキーが必要であることを特定します。ユーザーがAPIキーを提供後、Claude Codeはデータ取得サービスを記述します。
    *   **ダッシュボードの更新**: Claude CodeはAPIキーを使用して経済データをフェッチし、ダッシュボードを実際の情報で更新します。
    *   **Playwrightによる最終確認**: 実データが統合されたUIをPlaywrightで再度検証し、視覚的な整合性を確認します。

#### 成果

Claude CodeとMCPサーバーを組み合わせることで、数日かかる可能性のあるFigmaモックアップから機能的なデータ駆動型Webアプリケーションのフロントエンド開発が、数分で完了する可能性が示されます。

#ClaudeCode, #Figma, #Web開発