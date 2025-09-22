# HOW_TO_WRITE_A_NOTE.md

This document outlines all the markdown features and conventions supported in the `_notes/` directory based on analysis of existing functional programming wiki notes.

## Required Front Matter

Every note must start with YAML front matter containing a title:

```yaml
---
title: Your Note Title
---
```

The filename should match the title (e.g., `Your Note Title.md`).

## Supported Markdown Features

### 1. Headers

Use standard markdown headers:
```markdown
# Main Header
## Section Header
### Subsection Header
```

### 2. Wiki-style Links

Use double bracket notation for internal links to other notes:
```markdown
[[Note Title]]
[[Note Title|Display Text]]
```

Examples from the codebase:
- `[[Algebraic Data Type| Algebraic Data Type or ADT]]`
- `[[Sum Type]]`
- `[[I.Todo]]`

### 3. Code Blocks

#### Inline Code
Use backticks for inline code:
```markdown
`type Pair = Fst Int | Snd String`
```

#### Code Blocks with Language Syntax
Use triple backticks with language specification:

```markdown
```hs
data Lens a b = Lens (a -> b -> a) (a -> b)
```

```javascript
let map: (a => b) => Option(a) => Option(b) = f =>
    fun
    | Some(a) => Some(f(a))
    | None => None
```
```

Supported languages observed: `hs` (Haskell), JavaScript (no language tag)

### 4. Lists

#### Unordered Lists
```markdown
* Item one
* Item two
* Item three
```

#### Ordered Lists
```markdown
1. First item
2. Second item
3. Third item
```

### 5. Horizontal Rules

Use triple dashes to create section dividers:
```markdown
---
```

### 6. Block Quotes

Use `>` for quotations:
```markdown
> The names were imported from the Dreyfus model of skill acquisition
> [Source](https://twitter.com/lambda_conf/status/804439435261546496)
```

### 7. External Links

Standard markdown link syntax:
```markdown
[Link text](https://example.com)
```

### 8. Embedded Images

Reference images in the Attachments folder:
```markdown
![[image-filename.jpeg]]
```

Example: `![[standardized-ladder-of-functional-programming.jpeg]]`

### 9. Comments and Code Comments

JavaScript-style comments in code blocks:
```javascript
// Constructor usage
let a = Some(1);
// output: Some(2)
```

### 10. Mathematical Notation (MathJax)

While not directly observed in the sample files, the CLAUDE.md indicates MathJax support:
- Inline math: `$equation$`
- Block math: `$$equation$$`

## Note Type Conventions

Based on the naming conventions found:

### Documentation Notes
- Prefix: `D.`
- Example: `D.Template Note.md`

### Interface Notes
- Prefix: `I.`
- Example: `I.Todo.md`, `I.Exercise.md`

### Map of Content (MOC) Notes
- Prefix: `M.`
- Example: `M.Functional Programming Language.md`

### Template Notes
- Prefix: `T.`

### Concept Notes
- Capitalize each word
- Use noun phrases
- Example: `Algebraic Data Type.md`, `Higher Order Function.md`

### Proposition Notes
- Write as declarative sentences
- Keep titles short, avoid punctuation

## Type Signatures and Function Definitions

The notes support various programming language syntaxes:

```markdown
Haskell: `Functor f => (a -> b) -> f a -> f b`
JavaScript/ReasonML: `(a => b) => Option(a) => Option(b)`
```

## Content Organization

- Use horizontal rules (`---`) to separate sections
- Include examples after concept explanations
- Reference related concepts using wiki-links
- Include source citations with external links
- Use todo markers: `[[I.Todo]] : Description`

## Tags and Categories

Use wiki-links as implicit tags:
```markdown
[[I.Exercise]],
[[I.External]],
```

Note the trailing comma convention for tag-like references.