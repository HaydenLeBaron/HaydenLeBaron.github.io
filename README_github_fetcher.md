# GitHub Portfolio Data Fetcher

This script fetches your GitHub profile and repository data to serve as a single source of truth for your portfolio website.

==IMPORTANT: a repo must have >=1 star_gazers AND have a file titled README.md in the root directory in order to be included in the output==

## Setup

### Prerequisites
- Python 3.6+
- Internet connection

### GitHub Token (Recommended)
For higher rate limits, create a GitHub personal access token:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `public_repo` scope
3. Set as environment variable:
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```

## Usage

### Basic Usage
```bash
python3 fetch_github_data.py
```

### With Custom Options
```bash
# Custom username and output file
python3 fetch_github_data.py --username YourUsername --output my_data.json

# With token
python3 fetch_github_data.py --token your_github_token

# All options
python3 fetch_github_data.py --username HaydenLeBaron --token your_token --output github_portfolio.json
```

### Environment Variables
```bash
export GITHUB_TOKEN="your_token_here"     # GitHub personal access token
export GITHUB_USERNAME="HaydenLeBaron"    # GitHub username (optional)
```

## Output

The script generates a JSON file with:

- **Profile information**: bio, location, contact details, follower counts
- **All public repositories**: with languages, descriptions, topics, README URLs
- **Pinned repositories**: subset of repos marked as portfolio highlights
- **Repository metadata**: stars, forks, creation/update dates

### Sample Output Structure
```json
{
  "profile": {
    "login": "HaydenLeBaron",
    "name": "Hayden LeBaron",
    "bio": "Functional programming enthusiast...",
    "location": "Salt Lake City, Utah",
    "email": "me@haydenlebaron.com"
  },
  "nonpinned_repositories": [...],
  "pinned_repositories": [...],
  "fetched_at": "2024-01-15T10:30:00Z"
}
```

## Rate Limits

- **Without token**: 60 requests/hour
- **With token**: 5,000 requests/hour

The script handles rate limiting gracefully and will suggest using a token if limits are exceeded.

## Integration with Website

Run this script manually whenever you want to update your website with the latest GitHub data. The output JSON can be processed by other scripts or templates to generate website content.