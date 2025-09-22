#!/usr/bin/env python3
"""
GitHub Portfolio Data Fetcher

This script fetches portfolio data from GitHub API to update website content.
It serves as a single source of truth for portfolio projects and profile information.

Usage:
    python fetch_github_data.py [--token TOKEN] [--username USERNAME]

Environment Variables:
    GITHUB_PUBLIC_DATA_EDIT_PROFILE_TOKEN: GitHub personal access token (recommended for higher rate limits)
    GITHUB_USERNAME: GitHub username (defaults to 'HaydenLeBaron')
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
from typing import Dict, List, Optional, Any
from datetime import datetime


class GitHubFetcher:
    def __init__(self, username: str, token: Optional[str] = None):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"

    def _make_request(self, endpoint: str, critical: bool = True) -> Optional[Dict[str, Any]]:
        """Make authenticated request to GitHub API"""
        url = f"{self.base_url}/{endpoint}"
        req = urllib.request.Request(url)

        if self.token:
            req.add_header("Authorization", f"token {self.token}")

        req.add_header("Accept", "application/vnd.github.v3+json")
        req.add_header("User-Agent", "GitHub-Portfolio-Fetcher/1.0")

        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            if critical:
                print(f"HTTP Error {e.code}: {e.reason} for {url}")
                if e.code == 403:
                    print("Rate limit exceeded. Consider using a GitHub token.")
                sys.exit(1)
            else:
                return None
        except Exception as e:
            if critical:
                print(f"Error fetching {url}: {e}")
                sys.exit(1)
            else:
                return None

    def get_profile(self) -> Dict[str, Any]:
        """Fetch user profile information"""
        return self._make_request(f"users/{self.username}")

    def get_repositories(self) -> List[Dict[str, Any]]:
        """Fetch all public repositories"""
        repos = []
        page = 1
        per_page = 100

        while True:
            endpoint = f"users/{self.username}/repos?page={page}&per_page={per_page}&sort=updated"
            page_repos = self._make_request(endpoint)

            if not page_repos:
                break

            repos.extend(page_repos)

            if len(page_repos) < per_page:
                break

            page += 1

        return repos

    def get_pinned_repos(self) -> List[str]:
        """Get pinned repository names from GraphQL API (fallback to hardcoded list)"""
        # For the pinned repos, we'll use the ones specified in the markdown file
        # as the GraphQL API requires different authentication
        return [
            "provably-packed",
            "arezzo",
            "funxychat",
            "sweaty-tictactoe",
            "qs-location-dashboard",
            "delta-y-releases"
        ]

    def get_languages(self, repo_name: str) -> Dict[str, int]:
        """Get programming languages used in a repository"""
        result = self._make_request(f"repos/{self.username}/{repo_name}/languages", critical=False)
        return result if result else {}

    def get_readme_url(self, repo_name: str) -> Optional[str]:
        """Get README URL for a repository"""
        response = self._make_request(f"repos/{self.username}/{repo_name}/contents/README.md", critical=False)
        if response:
            return f"https://github.com/{self.username}/{repo_name}/blob/main/README.md"
        return None

    def fetch_portfolio_data(self) -> Dict[str, Any]:
        """Fetch complete portfolio data"""
        print(f"Fetching GitHub data for {self.username}...")

        # Get profile info
        print("Fetching profile...")
        profile = self.get_profile()

        # Get all repositories
        print("Fetching repositories...")
        all_repos = self.get_repositories()

        # Get pinned repository names
        pinned_repo_names = self.get_pinned_repos()

        # Process repositories
        print("Processing repository details...")
        all_repos_data = []
        pinned_repos_data = []

        for repo in all_repos:
            if repo['private']:
                continue

            repo_name = repo['name']
            print(f"  Processing {repo_name}...")

            # Get languages
            languages = self.get_languages(repo_name)

            # Get README URL
            readme_url = self.get_readme_url(repo_name)

            # Filter out repos with no stars or no README
            if repo['stargazers_count'] == 0 or readme_url is None:
                print(f"    Skipping {repo_name} (no stars or no README)")
                continue

            repo_data = {
                'name': repo_name,
                'full_name': repo['full_name'],
                'description': repo['description'],
                'html_url': repo['html_url'],
                'homepage': repo['homepage'],
                'topics': repo['topics'],
                'languages': languages,
                'readme_url': readme_url,
                'stargazers_count': repo['stargazers_count'],
                'forks_count': repo['forks_count'],
                'created_at': repo['created_at'],
                'updated_at': repo['updated_at'],
                'pushed_at': repo['pushed_at']
            }

            all_repos_data.append(repo_data)

            # Check if this is a pinned repo
            if repo_name in pinned_repo_names:
                pinned_repos_data.append(repo_data)

        # Filter out pinned repos from unpinned repos
        nonpinned_repos_data = [repo for repo in all_repos_data if repo['name'] not in pinned_repo_names]

        # Sort pinned repos by the order in pinned_repo_names
        pinned_repos_data.sort(key=lambda x: pinned_repo_names.index(x['name']))

        return {
            'profile': {
                'login': profile['login'],
                'name': profile['name'],
                'bio': profile['bio'],
                'location': profile['location'],
                'email': profile['email'],
                'blog': profile['blog'],
                'company': profile['company'],
                'html_url': profile['html_url'],
                'avatar_url': profile['avatar_url'],
                'public_repos': profile['public_repos'],
                'followers': profile['followers'],
                'following': profile['following'],
                'created_at': profile['created_at'],
                'updated_at': profile['updated_at']
            },
            'nonpinned_repositories': repos_data,
            'pinned_repositories': nonpinned_repos_data,
            'fetched_at': datetime.utcnow().isoformat() + 'Z'
        }


def main():
    parser = argparse.ArgumentParser(description='Fetch GitHub portfolio data')
    parser.add_argument('--token', help='GitHub personal access token')
    parser.add_argument('--username', default='HaydenLeBaron', help='GitHub username')
    parser.add_argument('--output', default='github_data.json', help='Output file path')

    args = parser.parse_args()

    # Get token from argument or environment
    token = args.token or os.getenv('GITHUB_PUBLIC_DATA_EDIT_PROFILE_TOKEN')

    # Create fetcher
    fetcher = GitHubFetcher(args.username, token)

    # Fetch data
    try:
        data = fetcher.fetch_portfolio_data()

        # Write to file
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nData successfully written to {args.output}")
        print(f"Found {len(data['nonpinned_repositories'])} nonpinned repositories")
        print(f"Found {len(data['pinned_repositories'])} pinned repositories")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()