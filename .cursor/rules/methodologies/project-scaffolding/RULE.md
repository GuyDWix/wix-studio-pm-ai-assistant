---
description: "Use when starting a new project, creating project structure, or initializing a new PM initiative"
alwaysApply: false
---

# Project Scaffolding Methodology

## When to Use
- Starting a new PM project
- Creating project folder structure
- Initializing new initiatives

## Lightning-Fast Project Creation

**[CRITICAL]: Follow these steps in THIS EXACT ORDER!**

### Step 1: Check for Existing Projects
- Look in `projects/` folder for potential duplicates
- If redundancy suspected, ask user: create new or reuse existing?

### Step 2: Create Basic Structure
```bash
mkdir -p projects/[simple-name]/context
mkdir -p projects/[simple-name]/output
```

### Step 3: Add Relevant Context
- Based on user intent, read relevant `@shared-knowledge/` files
- Always start with `@shared-knowledge/company-fundamentals.md`
- **KEY PRINCIPLE**: Start minimal. Add context only when gaps identified.

### Step 4: Notify User
- Confirm project was created
- Wait for further instructions

## Folder Structure

```
projects/[project-name]/
├── context/
│   └── <input materials, research, references>
└── output/
    └── <deliverables, artifacts, documentation>
```

## Best Practices
- Use kebab-case for project names
- Keep context folder for inputs, output folder for deliverables
- Reference shared-knowledge files rather than copying content
- Start with minimal context, expand as needed
