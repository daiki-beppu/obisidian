#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_frontmatter(content):
    """フロントマターと本文を分離"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    if not match:
        return None, content
    return match.group(1), match.group(2)

def parse_yaml_simple(yaml_text):
    """シンプルなYAMLパーサー（PyYAML不要）"""
    data = {}
    for line in yaml_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # リスト形式のタグを処理
            if key == 'tags' and '[' in value:
                # ['react', 'nextjs'] → ['react', 'nextjs']
                tags = re.findall(r"'([^']+)'", value)
                data[key] = tags
            else:
                data[key] = value
    return data

def extract_tags(frontmatter_data):
    """tagsフィールドからハッシュタグを生成"""
    tags = frontmatter_data.get('tags', [])
    if isinstance(tags, list):
        return [f"#{tag}" for tag in tags]
    return []

def remove_navigation_section(content):
    """ナビゲーションリンクセクションを削除"""
    # パターン: ## 🔗 このシリーズの学習パス から最後まで
    pattern = r'\n## 🔗 このシリーズの学習パス.*$'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content.rstrip() + '\n'

def convert_file(file_path):
    """単一ファイルの変換"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # フロントマター抽出
    frontmatter, body = extract_frontmatter(content)
    if frontmatter is None:
        print(f"⚠️  {file_path}: フロントマターなし、スキップ")
        return False

    # フロントマター解析
    data = parse_yaml_simple(frontmatter)

    # 必要なフィールド抽出
    title = data.get('title', '')
    created = data.get('created', '')
    updated = data.get('updated', '')

    if not all([title, created, updated]):
        print(f"⚠️  {file_path}: 必須フィールド不足")
        return False

    # タグ抽出
    tag_list = extract_tags(data)

    # 新しいフロントマター作成
    new_frontmatter = f"""---
title: {title}
created: {created}
updated: {updated}
---"""

    # ハッシュタグ作成
    hashtags = "#log #output " + " ".join(tag_list)

    # ナビゲーションリンク削除
    body = remove_navigation_section(body)

    # 新しいコンテンツ組み立て
    new_content = f"{new_frontmatter}\n\n{hashtags}\n\n{body}"

    # ファイル書き込み
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ {file_path.name}")
    return True

def main():
    log_dir = Path('/Users/mba/01-dev/obsidian-vault/tech-notes/log')
    md_files = list(log_dir.glob('*.md'))

    print(f"対象ファイル: {len(md_files)}個\n")

    success_count = 0
    for file_path in md_files:
        if convert_file(file_path):
            success_count += 1

    print(f"\n変換完了: {success_count}/{len(md_files)}個")

if __name__ == '__main__':
    main()
