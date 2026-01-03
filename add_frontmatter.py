#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

def has_frontmatter(content):
    """ファイルがフロントマターを持っているか確認"""
    pattern = r'^---\s*\n.*?\n---\s*\n'
    return bool(re.match(pattern, content, re.DOTALL))

def get_file_timestamps(file_path):
    """ファイルシステムのタイムスタンプから日付を取得"""
    stat = file_path.stat()

    # 作成日（created）
    # macOSではst_birthtimeが使える
    if hasattr(stat, 'st_birthtime'):
        created = datetime.fromtimestamp(stat.st_birthtime).strftime('%Y-%m-%d')
    else:
        # Linuxではst_ctimeを使用
        created = datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d')

    # 更新日（updated）
    updated = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')

    return created, updated

def add_frontmatter_to_file(file_path):
    """フロントマターがないファイルに追加"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # すでにフロントマターがある場合はスキップ
    if has_frontmatter(content):
        print(f"⏭️  {file_path.name}: フロントマターあり、スキップ")
        return False

    # ファイル名からtitleを生成（拡張子を除く）
    title = file_path.stem

    # タイムスタンプから日付を取得
    created, updated = get_file_timestamps(file_path)

    # 新しいフロントマター作成
    frontmatter = f"""---
title: {title}
created: {created}
updated: {updated}
---"""

    # ハッシュタグ
    hashtags = "#log #output"

    # 新しいコンテンツ組み立て
    new_content = f"{frontmatter}\n\n{hashtags}\n\n{content}"

    # ファイル書き込み
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ {file_path.name}")
    return True

def main():
    log_dir = Path('/Users/mba/01-dev/obsidian-vault/tech-notes/log')
    md_files = list(log_dir.glob('*.md'))

    # スクリプト自体やディレクトリを除外
    md_files = [f for f in md_files if f.is_file()]

    print(f"対象ファイル: {len(md_files)}個\n")

    success_count = 0
    skip_count = 0

    for file_path in md_files:
        result = add_frontmatter_to_file(file_path)
        if result:
            success_count += 1
        else:
            skip_count += 1

    print(f"\nフロントマター追加完了: {success_count}個")
    print(f"スキップ（既にフロントマターあり）: {skip_count}個")

if __name__ == '__main__':
    main()
