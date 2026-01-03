---
source: "https://techblog.sakurug.co.jp/article/obsidian_notebooklm_googledrive/#h4aacea989b"
published: 2025-12-08
created: 2026-01-03
---
#データ

## Obsidian×NotebookLMによるAI時代のインプット・アウトプット方法

この記事では、ObsidianとNotebookLMを組み合わせ、AIを活用して知識のインプットとアウトプットの質と量を効率的に向上させる方法を紹介します。

### 1. ツール選定の理由

*   **Obsidian**: ローカルファーストでプライバシーが保護され、Markdown形式での管理やGit連携が容易な「知識のローカルDB」。複雑なリンク構造は避け、タグ（#ログ、#データ）によるシンプルな管理を目指す。
*   **NotebookLM**: Google Drive内のファイルを学習ソースとして取り込み、多様な方法でインプット・アウトプットを支援。「AIによる加速」を担当。
*   **Google Drive**: ObsidianのVaultを安全に同期し、NotebookLMとの連携を容易にする。

### 2. 知識循環フロー

1.  **入力と分類（Web Clipper → Obsidian）**: Web Clipperで収集した情報をObsidianに記録し、#データ タグなどで分類。
2.  **過去のインプット把握（Obsidian Dataview）**: デイリーノートに設定したDataviewクエリで、過去に作成したインプットノートを自動表示し、今日の学習テーマを発掘。
3.  **AIによる加速とアウトプット生成（NotebookLM）**: DataviewでリストアップされたノートをNotebookLMにアップロードし、多様な方法で学習・アウトプット。
4.  **アウトプットのログ化**: NotebookLMでのアウトプット結果を#ログ タグを付けて記録し、学習履歴として蓄積。

### 3. 設定手順

*   **Obsidian Web Clipper**: ブラウザ拡張機能の設定。
*   **Obsidian Dataview**: コアプラグインとコミュニティプラグインを有効化し、デイリーノートテンプレートにDataviewクエリを設定。過去のインプットノートを自動表示させる。

#AI #Obsidian #NotebookLM