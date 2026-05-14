#!/usr/bin/env python3
"""
Lizer Daily Lab Builder
每天自动探索新技术，开发小项目并发布到 GitHub
"""

import json
import os
import subprocess
import urllib.request
import urllib.error
import re
import unicodedata
from datetime import datetime
from pathlib import Path

LABS_DIR = Path("/root/projects/daily-labs/labs")
GITHUB_BASE = "git@github.com:LizerAIDev"


def fetch_hn_stories(limit=15):
    """获取 Hacker News 热门技术故事"""
    try:
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        with urllib.request.urlopen(url, timeout=5) as resp:
            story_ids = json.loads(resp.read())[:limit]
        
        stories = []
        for sid in story_ids[:5]:  # 只取前5个
            try:
                story_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
                with urllib.request.urlopen(story_url, timeout=3) as resp:
                    stories.append(json.loads(resp.read()))
            except:
                continue
        return stories
    except Exception as e:
        print(f"[WARN] HN fetch failed: {e}")
        return []


def fetch_github_trending():
    """获取 GitHub 热门仓库趋势"""
    try:
        url = "https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc&per_page=10".format(
            (datetime.now()).strftime("%Y-%m-%d")
        )
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        return data.get("items", [])
    except Exception as e:
        print(f"[WARN] GitHub trending fetch failed: {e}")
        return []


def pick_topic(stories, trending):
    """从获取的信息中选择一个有趣的技术方向"""
    topics = []
    
    # 从 HN 提取
    for s in stories:
        if s.get("title"):
            topics.append({
                "source": "HN",
                "title": s["title"],
                "url": s.get("url", ""),
                "score": s.get("score", 0)
            })
    
    # 从 GitHub trending 提取
    for r in trending:
        if r.get("name"):
            topics.append({
                "source": "GitHub",
                "title": f"{r['name']} - {r.get('description', '')}",
                "url": r.get("html_url", ""),
                "score": r.get("stargazers_count", 0)
            })
    
    if not topics:
        # Fallback: 默认项目创意
        fallbacks = [
            {"title": "AI 驱动的每日新闻摘要工具", "url": "", "score": 0, "source": "Lizer创意"},
            {"title": "实时天气可视化仪表板", "url": "", "score": 0, "source": "Lizer创意"},
            {"title": "Markdown 转交互式幻灯片", "url": "", "score": 0, "source": "Lizer创意"},
        ]
        topics.extend(fallbacks)
    
    # 选 score 最高的
    return max(topics, key=lambda x: x["score"])


def create_lab(topic):
    """创建每日 lab 项目"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    # 转换为 ASCII 兼容的 slug
    title = topic["title"]
    # 移除非 ASCII 字符，保留字母数字
    slug = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', slug).strip('-').lower()[:40]
    lab_name = f"{date_str}-{slug}" if slug else f"{date_str}-daily-lab"
    lab_path = LABS_DIR / lab_name
    
    # 创建项目结构
    lab_path.mkdir(parents=True, exist_ok=True)
    
    # README
    readme = f"""# {topic['title']}

> Lizer Daily Lab - {date_str}
> 
> 来源: {topic['url'] if topic['url'] else 'Lizer 创意'}

## 快速开始
```bash
python main.py
```

## 功能
- [ ] 核心功能实现中...

---
*由 Lizer 自主开发*
"""
    (lab_path / "README.md").write_text(readme)
    
    # Python 主程序模板
    main_py = '''#!/usr/bin/env python3
"""
Lizer Daily Lab - {title}
"""

def main():
    print("🧪 {title}")
    print("=" * 40)
    # TODO: 实现核心逻辑
    print("项目已就绪！")

if __name__ == "__main__":
    main()
'''.format(title=topic["title"])
    (lab_path / "main.py").write_text(main_py)
    
    return lab_name


def push_to_github(lab_name):
    """推送到 GitHub"""
    lab_path = LABS_DIR / lab_name
    
    commands = [
        f"cd {lab_path} && git init -b main",
        f"cd {lab_path} && git add .",
        f'cd {lab_path} && git commit -m "🧪 Daily Lab: {lab_name} by Lizer"',
        f"cd {lab_path} && git remote add origin {GITHUB_BASE}/{lab_name}.git",
        f"cd {lab_path} && git push -u origin main",
    ]
    
    for cmd in commands:
        print(f"[EXEC] {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr and result.returncode != 0:
            print(f"[ERROR] {result.stderr}")
            return False
    
    print(f"[SUCCESS] Pushed to https://github.com/LizerAIDev/{lab_name}")
    return True


def main():
    print("=" * 50)
    print("🤖 Lizer Daily Lab Builder")
    print("=" * 50)
    
    # 1. 获取信息
    print("\n[1/4] Fetching Hacker News stories...")
    stories = fetch_hn_stories()
    
    print("[2/4] Fetching GitHub trending...")
    trending = fetch_github_trending()
    
    # 2. 选择主题
    print("[3/4] Picking interesting topic...")
    topic = pick_topic(stories, trending)
    print(f"  → 选择: {topic['title']}")
    print(f"  → 来源: {topic['source']} (score: {topic['score']})")
    
    # 3. 创建项目
    lab_name = create_lab(topic)
    print(f"[4/4] Created lab: {lab_name}")
    
    # 4. 推送 (可选，取决于是否有 GitHub token)
    print("\n📦 项目已创建，准备推送...")
    push_to_github(lab_name)
    
    print("\n" + "=" * 50)
    print("✅ Daily Lab 完成！")


if __name__ == "__main__":
    main()
