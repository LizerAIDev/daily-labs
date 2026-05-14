#!/usr/bin/env python3
"""
Lizer Daily Runner - 每日自主执行：探索→开发→发布
Runs via cron: every day at 9:00 AM UTC
"""

import json
import subprocess
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/root/projects")
GITHUB_USER = "LizerAIDev"
GITHUB_EMAIL = "buker2019@gmail.com"

IDEAS = [
    {"name": "url-screenshot", "desc": "CLI tool to take screenshots of web pages", "lang": "python"},
    {"name": "json-diff-cli", "desc": "Colorized JSON diff for terminal", "lang": "python"},
    {"name": "readme-generator", "desc": "Generate beautiful READMEs from templates", "lang": "python"},
    {"name": "csv-to-sqlite", "desc": "Convert CSV files to SQLite databases with a CLI", "lang": "python"},
    {"name": "git-quick-stats", "desc": "Quick git repository statistics without external deps", "lang": "python"},
    {"name": "dotenv-merge", "desc": "Merge and validate multiple .env files", "lang": "python"},
    {"name": "cron-parser", "desc": "Human-readable cron expression parser", "lang": "python"},
    {"name": "http-ping", "desc": "HTTP endpoint monitoring tool", "lang": "python"},
    {"name": "text-statistics", "desc": "CLI text analysis: word count, readability, complexity", "lang": "python"},
    {"name": "emoji-search", "desc": "Search and copy emojis from terminal", "lang": "python"},
    {"name": "docker-port-check", "desc": "Check which ports are in use by Docker containers", "lang": "python"},
    {"name": "yaml-to-json", "desc": "Fast YAML to JSON converter with validation", "lang": "python"},
    {"name": "code-counter", "desc": "Count lines of code by language in a project", "lang": "python"},
    {"name": "markdown-toc", "desc": "Generate table of contents for Markdown files", "lang": "python"},
    {"name": "json-pretty", "desc": "Pretty print and validate JSON files from CLI", "lang": "python"},
]


def get_used_names():
    """Get names of existing repos to avoid duplicates"""
    try:
        url = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            repos = json.loads(resp.read())
        return {r["name"].lower() for r in repos}
    except:
        return set()


def pick_idea(used):
    """Pick a project that hasn't been created yet"""
    for idea in IDEAS:
        if idea["name"].lower() not in used:
            return idea
    # Fallback: timestamped project
    return {
        "name": f"daily-lab-{datetime.now().strftime('%Y%m%d')}",
        "desc": f"Daily lab by Lizer - {datetime.now().strftime('%Y-%m-%d')}",
        "lang": "python"
    }


def create_project(idea):
    """Create a new project with basic structure"""
    project_dir = BASE_DIR / idea["name"]
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # main.py
    main_content = f'''#!/usr/bin/env python3
"""
{idea['desc']}
By Lizer - https://github.com/{GITHUB_USER}
"""


def main():
    print("{idea['name']} v0.1.0")
    print("=" * 40)
    print("Project initialized. Add your code here!")
    # TODO: implement core functionality


if __name__ == "__main__":
    main()
'''
    (project_dir / "main.py").write_text(main_content)
    
    # README.md
    readme = f"""# {idea['name']}

{idea['desc']}

## Quick Start

```bash
python main.py
```

## Features

- [ ] Core functionality

## License

MIT

---

*By Lizer - [github.com/{GITHUB_USER}](https://github.com/{GITHUB_USER})*
"""
    (project_dir / "README.md").write_text(readme)
    
    return project_dir


def push_to_github(project_dir, idea):
    """Create repo and push"""
    cmds = [
        f"cd {project_dir} && git init -b main",
        f"cd {project_dir} && git config user.name '{GITHUB_USER}'",
        f"cd {project_dir} && git config user.email '{GITHUB_EMAIL}'",
        f"cd {project_dir} && git add -A",
        f'cd {project_dir} && git commit -m "feat: initial commit - {idea["desc"]}"',
        f"cd {project_dir} && gh repo create {GITHUB_USER}/{idea['name']} --public --source . --remote origin --push",
    ]
    
    for cmd in cmds:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0 and "already exists" not in result.stderr:
            print(f"[ERROR] {cmd}\n{result.stderr}")
            return False
    
    print(f"[SUCCESS] https://github.com/{GITHUB_USER}/{idea['name']}")
    return True


def find_good_first_issue():
    """Find a good first issue to contribute to"""
    try:
        url = "https://api.github.com/search/issues?q=label:%22good+first+issue%22+state:open&sort=updated&order=desc&per_page=10"
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        return data.get("items", [])[:3]
    except:
        return []


def main():
    print(f"\n{'='*50}")
    print(f"  Lizer Daily Run - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*50}\n")
    
    # 1. Create a new project
    print("[1/2] Creating new project...")
    used = get_used_names()
    idea = pick_idea(used)
    print(f"  Idea: {idea['name']} - {idea['desc']}")
    
    project_dir = create_project(idea)
    push_to_github(project_dir, idea)
    
    # 2. Find issues to contribute
    print("\n[2/2] Finding issues to contribute...")
    issues = find_good_first_issue()
    if issues:
        print(f"  Found {len(issues)} potential issues:")
        for issue in issues:
            print(f"    - {issue['repository_url'].split('/')[-1]}#{issue['number']}: {issue['title'][:60]}")
    
    print(f"\n{'='*50}")
    print(f"  Daily run complete!")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
