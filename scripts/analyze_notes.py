#!/usr/bin/env python3
"""
Obsidian vault のノートを分析して、タグとフロントマターを収集するスクリプト
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set


def extract_frontmatter(content: str) -> Dict[str, str]:
    """フロントマターを抽出"""
    frontmatter = {}
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        fm_content = match.group(1)
        for line in fm_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"')

    return frontmatter


def extract_tags(content: str) -> Set[str]:
    """タグを抽出（# で始まる行とフロントマター内のタグ）"""
    tags = set()

    # # で始まるタグを抽出
    tag_pattern = r'#(\w+(?:-\w+)*)'
    matches = re.findall(tag_pattern, content)
    tags.update(matches)

    return tags


def extract_links(content: str) -> List[str]:
    """双方向リンク [[...]] を抽出"""
    link_pattern = r'\[\[([^\]]+)\]\]'
    links = re.findall(link_pattern, content)
    return links


def analyze_file(file_path: Path) -> Dict:
    """ファイルを分析して情報を返す"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter = extract_frontmatter(content)
        tags = extract_tags(content)
        links = extract_links(content)

        # ファイル名から拡張子を除く
        filename = file_path.stem

        return {
            'path': str(file_path.relative_to(Path.cwd())),
            'filename': filename,
            'title': frontmatter.get('title', filename),
            'created': frontmatter.get('created', ''),
            'updated': frontmatter.get('updated', ''),
            'tags': sorted(list(tags)),
            'links': links,
            'frontmatter': frontmatter
        }
    except Exception as e:
        print(f"エラー: {file_path} - {e}")
        return None


def analyze_vault(base_dir: Path, exclude_dirs: List[str] = None) -> Dict[str, Dict]:
    """Vault全体を分析"""
    if exclude_dirs is None:
        exclude_dirs = ['daily', 'templates', '.git', '.obsidian']

    results = {}

    # log/ と data/ のファイルを分析
    for directory in ['log', 'data']:
        dir_path = base_dir / directory
        if not dir_path.exists():
            continue

        for md_file in dir_path.glob('*.md'):
            file_info = analyze_file(md_file)
            if file_info:
                results[file_info['filename']] = file_info

    return results


def group_by_tags(results: Dict[str, Dict]) -> Dict[str, List[str]]:
    """タグごとにファイルをグループ化"""
    tag_groups = {}

    for filename, info in results.items():
        for tag in info['tags']:
            if tag not in tag_groups:
                tag_groups[tag] = []
            tag_groups[tag].append(filename)

    return tag_groups


def find_related_files(results: Dict[str, Dict], min_common_tags: int = 2) -> Dict[str, List[Dict]]:
    """関連するファイルを見つける（共通タグが多いもの）"""
    related = {}

    for filename1, info1 in results.items():
        related[filename1] = []
        tags1 = set(info1['tags'])

        for filename2, info2 in results.items():
            if filename1 == filename2:
                continue

            tags2 = set(info2['tags'])
            common_tags = tags1 & tags2

            if len(common_tags) >= min_common_tags:
                related[filename1].append({
                    'filename': filename2,
                    'common_tags': sorted(list(common_tags)),
                    'score': len(common_tags)
                })

        # スコアでソート
        related[filename1].sort(key=lambda x: x['score'], reverse=True)

    return related


def main():
    base_dir = Path.cwd()

    print("📊 Vault分析を開始します...")
    results = analyze_vault(base_dir)

    print(f"\n✅ {len(results)} 個のファイルを分析しました\n")

    # タグごとのグループ化
    tag_groups = group_by_tags(results)

    print("📌 タグの一覧:")
    for tag, files in sorted(tag_groups.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  #{tag}: {len(files)}個のファイル")

    # 関連ファイルの検出
    print("\n🔗 関連性の高いファイルを検出中...")
    related = find_related_files(results, min_common_tags=2)

    # 結果をJSONとして保存
    output_file = base_dir / 'scripts' / 'analysis_result.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'files': results,
            'tag_groups': tag_groups,
            'related': related
        }, f, ensure_ascii=False, indent=2)

    print(f"\n💾 分析結果を保存しました: {output_file}")

    # 関連性の高いファイル（リンクされていないもの）を表示
    print("\n🎯 リンク候補（関連性が高いがまだリンクされていないファイル）:")

    link_suggestions = []
    for filename, relations in related.items():
        if not relations:
            continue

        file_info = results[filename]
        existing_links = set(file_info['links'])

        for rel in relations[:5]:  # 上位5件
            if rel['filename'] not in existing_links:
                link_suggestions.append({
                    'from': filename,
                    'to': rel['filename'],
                    'common_tags': rel['common_tags'],
                    'score': rel['score']
                })

    # スコアでソート
    link_suggestions.sort(key=lambda x: x['score'], reverse=True)

    # 上位20件を表示
    for i, suggestion in enumerate(link_suggestions[:20], 1):
        print(f"\n{i}. {suggestion['from']}")
        print(f"   → {suggestion['to']}")
        print(f"   共通タグ: {', '.join(f'#{tag}' for tag in suggestion['common_tags'])}")
        print(f"   スコア: {suggestion['score']}")


if __name__ == '__main__':
    main()
