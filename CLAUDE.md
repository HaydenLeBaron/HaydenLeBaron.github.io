# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based digital garden/Zettelkasten for a software engineer's professional portfolio site. The site features:
- Individual notes in Markdown format stored in `_notes/`
- Interactive graph visualization of note connections using D3.js
- Backlink system showing relationships between notes
- MathJax support for mathematical notation
- Dark theme styling

## Key Architecture

### Jekyll Configuration
- Uses Jekyll 4.x with Ruby gems managed via Bundler
- Custom collections for notes (`_notes/`) with permalink structure `/:slug`
- Sass compilation with compressed output
- Jekyll plugin: `jekyll-last-modified-at` for tracking note updates

### Layout Structure
- `_layouts/note.html`: Main note template with backlinks sidebar and graph visualization
- `_layouts/default.html`: Base layout
- `_layouts/page.html`: For static pages
- `_includes/notes_graph.html`: D3.js interactive graph component
- `_includes/notes_graph.json`: Graph data structure for visualization

### Note System
- Notes are Markdown files in `_notes/` directory
- Backlink system automatically discovers and displays note relationships
- Graph visualization shows all notes and their connections
- MathJax integration for mathematical expressions

## Development Commands

### Local Development
```bash
# Install dependencies
bundle install

# Serve site locally with auto-reload
bundle exec jekyll serve

# Build site for production
bundle exec jekyll build

# Clean generated files
bundle exec jekyll clean
```

### Common Jekyll Commands
```bash
# Serve with specific configuration
bundle exec jekyll serve --config _config.yml

# Build with trace for debugging
bundle exec jekyll build --trace

# Serve with drafts included
bundle exec jekyll serve --drafts
```

## File Structure

### Core Directories
- `_notes/`: Markdown notes for the digital garden
- `_layouts/`: Jekyll layout templates
- `_includes/`: Reusable template components
- `_pages/`: Static pages (index, about)
- `_sass/`: Sass stylesheets
- `_site/`: Generated site output (Git ignored)

### Key Files
- `_config.yml`: Jekyll configuration
- `Gemfile`: Ruby dependencies
- `_includes/notes_graph.html`: D3.js graph visualization component (300+ lines)
- `_layouts/note.html`: Note template with backlinks and graph

## Graph Visualization

The site includes a sophisticated D3.js-based graph visualization that:
- Shows all notes as interconnected nodes
- Highlights related notes on hover
- Supports zooming and panning
- Uses force-directed layout with collision detection
- Node sizes reflect connection count
- Click navigation to notes

Graph data is generated in `_includes/notes_graph.json` and consumed by the D3.js component.

## Content Guidelines

- Notes should be in Markdown format in `_notes/`
- Use standard wikilink syntax `[[Note Title]]` for internal links
- Mathematical expressions use MathJax syntax with `$...$` for inline and `$$...$$` for block
- Each note gets automatic backlink discovery and graph inclusion