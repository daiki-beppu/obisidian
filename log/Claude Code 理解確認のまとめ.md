---
title: Claude Code 理解確認のまとめ
created: 2026-01-05
updated: 2026-01-05
---

このドキュメントは [[2026-01-03T220846+0900_データ_Claude Code Best Practices|Claude Code Best Practices]] および DeepLearning.AI のコース資料（[[2026-01-04T154928+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|並行開発]]、[[2026-01-04T155446+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|GitHub連携]]、[[2026-01-04T160154+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|コマンド一覧]]）の理解確認セッションです。

**第1回：プロジェクトメモリの基本**

• **質問：** Claude Codeを使い始める際、コードベースをスキャンしてプロジェクトのガイドラインを管理する「プロジェクトメモリ」として機能する**ファイルの名前**と、それを作成する**コマンド**は何でしょうか？

• **ユーザーの回答：** ファイル名: **CLAUDE.md** / コマンド: **/init**

• **解説：** **/init** コマンドを実行すると、プロジェクトをスキャンして **CLAUDE.md** が生成されます。このファイルは常にコンテキストに含まれ、Claude Codeへの重要なガイドとして機能します。詳細は [[2026-01-03T220846+0900_データ_Claude Code Best Practices|Best Practices]] で解説されています。

**第2回：カスタムコマンドの定義**

• **質問：** カスタムコマンドを定義するファイルはどの**フォルダ**に保存しますか？また、**CLAUDE.md** **との違い**は何ですか？

• **ユーザーの回答：** **.claude/commands** 配下に記述 / **ユーザーが明示的に指定したタイミング**で使用される

• **解説：** カスタムコマンドは **.claude/commands** フォルダ内にMarkdownファイルとして作成します。常にコンテキストに含まれる `CLAUDE.md` とは異なり、特定の会話の中で必要な時にのみ呼び出されます。カスタムコマンドの実践例は [[2026-01-04T154928+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|並行開発のレッスン]] でも紹介されています。

**第3回：自動化のためのフック機能**

• **質問：** フックの設定を管理する**コマンド**と、**フックがトリガーされるイベント（タイミング）**の具体例を2つ挙げてください。

• **ユーザーの回答：** **/hooks** / **Claudeが止まったタイミング**、**Claudeが承認を求めたタイミング**

• **解説：** **/hooks** コマンドで設定を管理します。イベントの具体例としては、**Stop**（停止時）や **UserPrompt**（ユーザーのプロンプト送信時）、**Before/PostToolUse**（ツール実行の前/後）などがあります。フック機能の詳細は [[2026-01-04T155446+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|GitHub連携とフックのレッスン]] で解説されています。

**第4回：GitHub連携と自動修復**

• **質問：** GitHub連携を導入する**コマンド**と、**GitHub Issuesでタグ付けされた際のプロセス**を教えてください。

• **ユーザーの回答：** **/install-github-app** / **CLAUDE.md** **と Issue を確認して**

• **解説：** **/install-GitHub-app** を使用して連携します。GitHub Issueでタグ付けされると、Claudeは問題を分析して計画を立て、修正を行い、最終的に**プルリクエスト（PR）を生成**します。このワークフローの詳細は [[2026-01-04T155446+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|GitHub連携のレッスン]] で実践的に紹介されています。

**第5回：Git Worktreesによる並行開発**

• **質問：** 並行開発を実現するための**Gitの機能名**、使用する**コマンド**、およびワークツリーが配置される**フォルダ**は何ですか？

• **ユーザーの回答：** **Git-working-tree** / **working/**（※正解は `.trees`）

• **解説：** **Git Worktrees** を利用します。**git worktree add** コマンドを使用して、**.trees** フォルダ内に独立した作業領域を作成することで、同じファイルを上書きせずに複数の機能を並行して開発できます。この並行開発の手法は [[2026-01-04T154928+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|並行開発のレッスン]] で詳しく解説されています。

--------------------------------------------------------------------------------

**全体を通した学習のポイント：** 今回の対話を通じて、[[2026-01-03T220846+0900_データ_Claude Code Best Practices|Best Practices]] や [[2026-01-04T160154+0900_データ_Claude Code A Highly Agentic Coding Assistant - DeepLearning.AI|DeepLearning.AI コース資料]] で学んだように、Claude Codeが単なるチャットAIではなく、**プロジェクト独自のルール（CLAUDE.md）**を理解し、**特定のタイミング（フック）****Gitの高度な機能（Worktrees）****GitHubのワークフロー**と密接に連携する「自律的なコーディングアシスタント」であることを確認できました。