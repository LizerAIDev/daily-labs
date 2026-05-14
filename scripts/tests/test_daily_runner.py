#!/usr/bin/env python3
"""Tests for daily-labs/scripts/daily_runner.py"""
import sys
import os
import json
import tempfile
import shutil
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import daily_runner


class TestGetUsedNames:
    @patch("urllib.request.urlopen")
    def test_returns_repo_names(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps([
            {"name": "repo-a"},
            {"name": "Repo-B"},
            {"name": "REPO-C"},
        ]).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        result = daily_runner.get_used_names()
        assert result == {"repo-a", "repo-b", "repo-c"}

    @patch("urllib.request.urlopen")
    def test_handles_per_page_param(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps([]).encode()
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        daily_runner.get_used_names()
        # urlopen is called with a Request object; check full_url
        req = mock_urlopen.call_args[0][0]
        assert "per_page=100" in req.full_url

    @patch("urllib.request.urlopen")
    def test_returns_empty_on_error(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Network error")
        result = daily_runner.get_used_names()
        assert result == set()


class TestPickIdea:
    def test_picks_first_unused(self):
        used = {"url-screenshot"}
        result = daily_runner.pick_idea(used)
        assert result["name"] == "json-diff-cli"

    def test_picks_first_when_none_used(self):
        used = set()
        result = daily_runner.pick_idea(used)
        assert result["name"] == "url-screenshot"

    def test_fallback_when_all_used(self):
        used = {idea["name"].lower() for idea in daily_runner.IDEAS}
        result = daily_runner.pick_idea(used)
        assert result["name"].startswith("daily-lab-")
        assert "desc" in result
        assert "lang" in result
        assert result["lang"] == "python"

    def test_fallback_has_today_date(self):
        used = {idea["name"].lower() for idea in daily_runner.IDEAS}
        result = daily_runner.pick_idea(used)
        today = datetime.now().strftime("%Y%m%d")
        assert today in result["name"]


class TestCreateProject:
    def setup_method(self):
        self.tmpdir = tempfile.mkdtemp()
        self.original_base = daily_runner.BASE_DIR
        daily_runner.BASE_DIR = Path(self.tmpdir)

    def teardown_method(self):
        daily_runner.BASE_DIR = self.original_base
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_creates_directory(self):
        idea = {"name": "test-project", "desc": "Test desc", "lang": "python"}
        result = daily_runner.create_project(idea)
        assert os.path.isdir(os.path.join(self.tmpdir, "test-project"))

    def test_creates_main_py(self):
        idea = {"name": "test-project", "desc": "Test desc", "lang": "python"}
        daily_runner.create_project(idea)
        main_path = os.path.join(self.tmpdir, "test-project", "main.py")
        assert os.path.isfile(main_path)
        content = open(main_path).read()
        assert "Test desc" in content
        assert "test-project v0.1.0" in content
        assert "LizerAIDev" in content

    def test_creates_readme(self):
        idea = {"name": "test-project", "desc": "Test desc", "lang": "python"}
        daily_runner.create_project(idea)
        readme_path = os.path.join(self.tmpdir, "test-project", "README.md")
        assert os.path.isfile(readme_path)
        content = open(readme_path).read()
        assert "test-project" in content
        assert "Test desc" in content
        assert "Quick Start" in content
        assert "LizerAIDev" in content

    def test_existing_directory_not_error(self):
        idea = {"name": "test-project", "desc": "Test desc", "lang": "python"}
        os.makedirs(os.path.join(self.tmpdir, "test-project"))
        result = daily_runner.create_project(idea)
        assert os.path.isdir(os.path.join(self.tmpdir, "test-project"))

    def test_returns_path(self):
        idea = {"name": "test-project", "desc": "Test desc", "lang": "python"}
        result = daily_runner.create_project(idea)
        assert result is not None


class TestIdeas:
    def test_ideas_structure(self):
        for idea in daily_runner.IDEAS:
            assert "name" in idea
            assert "desc" in idea
            assert "lang" in idea
            assert idea["lang"] == "python"

    def test_no_duplicate_names(self):
        names = [idea["name"].lower() for idea in daily_runner.IDEAS]
        assert len(names) == len(set(names))
