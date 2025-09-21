# Hayden LeBaron's Portfolio Site

This is a Jekyll-based portfolio website hosted on GitHub Pages, built using the [modern-resume-theme](https://github.com/sproogen/resume-theme).

## Prerequisites

- **Ruby** (version 2.7 or higher)
- **Bundler** gem
- **Git**

## Local Development Setup

### 1. Install Ruby and Bundler

**macOS (using Homebrew):**
```bash
brew install ruby
gem install bundler
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
gem install bundler
```

**Windows:**
- Download and install Ruby from [RubyInstaller](https://rubyinstaller.org/)
- Run `gem install bundler` in Command Prompt

### 2. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/HaydenLeBaron/HaydenLeBaron.github.io.git
cd HaydenLeBaron.github.io

# Install dependencies
bundle install
```

### 3. Run Locally

```bash
# Start the development server
bundle exec jekyll serve

# Or with live reload and drafts
bundle exec jekyll serve --livereload --drafts
```

The site will be available at `http://localhost:4000`

### 4. Making Changes

- **Content**: Edit `_config.yml` to update personal information, experience, projects, etc.
- **Styling**: Customize styles in the `_sass` directory
- **Images**: Add images to the `images/` directory

## Deployment

This site is automatically deployed via GitHub Pages when changes are pushed to the `main` branch.

### Manual Deployment Steps:

1. **Make your changes** and test locally
2. **Commit changes:**
   ```bash
   git add .
   git commit -m "Your commit message"
   ```
3. **Push to GitHub:**
   ```bash
   git push origin main
   ```
4. **GitHub Pages will automatically build and deploy** your site (usually takes 1-2 minutes)

## Site Configuration

The main configuration is in `_config.yml`. Key sections include:

- **Personal Info**: Name, title, email, social links
- **About Section**: Profile image and bio
- **Content Sections**: Experience, education, projects
- **Theme Settings**: Dark mode, additional links

## Common Commands

```bash
# Install dependencies
bundle install

# Update dependencies
bundle update

# Serve locally
bundle exec jekyll serve

# Serve with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Check for dependency vulnerabilities
bundle audit
```

## Troubleshooting

### Bundle Install Issues
```bash
# Clear bundle cache
bundle clean --force
bundle install
```

### Jekyll Version Conflicts
```bash
# Use GitHub Pages compatible versions
bundle update github-pages
```

### Permission Errors (macOS/Linux)
```bash
# Install gems to user directory
bundle install --path vendor/bundle
```

## Theme Documentation

This site uses the [modern-resume-theme](https://github.com/sproogen/resume-theme). For detailed theme documentation and customization options, visit the theme's repository.

## Contact

For questions about this site, contact Hayden LeBaron at [me@haydenlebaron.com](mailto:me@haydenlebaron.com).