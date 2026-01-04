---
source: "https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/33kzr/refactoring-a-jupyter-notebook-%26-creating-a-dashboard"
published: 2025-08-06
created: 2026-01-04
---
#データ

#ClaudeCode, #JupyterNotebook, #Streamlit

## Claude Code による Jupyter Notebook のリファクタリングと Streamlit ダッシュボード化

### 1. Jupyter Notebook のリファクタリング

*   **課題**: 散らかったeコマースデータノートブック、視覚化の表示が不十分、ビジネスロジックとプレゼンテーションが混在。
*   **目的**: データ処理、メトリクス計算、視覚化を分離し、より整理されたノートブックを作成。
*   **Claude Code への指示**: 
    *   データローディングと処理用のPythonファイルを作成。
    *   メトリクス計算用のPythonファイルを作成。
    *   視覚化の改善と設定の柔軟性を要求。
    *   依存関係 (`requirements.txt`) と使用方法 (`README`) を含める。
*   **Claude Code のプロセス**: 
    *   ノートブックを読み込み、構造を分析し、リファクタリング。
    *   `data_loader.py`、`business_metrics.py`、`requirements.txt`、`README.md` を生成。
    *   初期段階で発生した `KeyError` を修正指示により解決。
*   **結果**: オブジェクト指向のアプローチでクリーンなコードベースが構築され、視覚的に優れた分析と柔軟な設定が可能に。

### 2. Streamlit ダッシュボードへの変換

*   **目的**: リファクタリングされたノートブックをStreamlitベースのインタラクティブなダッシュボードに変換。
*   **Claude Code への指示**: 
    *   特定のレイアウト（ヘッダー、タイトル、フィルター、KPIカード、チャート）を持つStreamlitダッシュボードを作成。
    *   「売上」「成長」「平均注文額」「総注文数」のKPIカードを含める。
    *   「売上」「カテゴリ」「地域別売上」「顧客満足度」のチャートを含める。
*   **Claude Code のプロセス**: 
    *   `dashboard.py` ファイルを生成し、必要なライブラリ（Streamlit, pandas, Plotly）をインポート。
    *   CSSによるスタイリングとページ設定を実施。
    *   `requirements.txt` と `README.md` を更新。
*   **初期ダッシュボードの課題と改善**: 
    *   初期ダッシュボードには空のカードや冗長な情報、不適切なデフォルト年（2024年）といった問題があった。
    *   **Claude Code への修正指示**: 
        *   デフォルトの年を2023年に設定。
        *   月フィルターを追加。
        *   空のカードを削除。
*   **結果**: より洗練されたダッシュボードが完成し、チーム内での共有や迅速な反復が可能になる。

