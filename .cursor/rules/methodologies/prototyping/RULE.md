---
description: "Use when creating interactive prototypes, lo-fi mockups, tractors for flow validation, or visual PRDs for stakeholder alignment before design investment"
alwaysApply: false
---

# Prototyping Methodology (Tractors)

## When to Use
- Validating product flows before design investment
- Creating interactive click-through experiences
- Aligning stakeholders on functionality
- Building "visual PRDs" for review

## What is a Tractor?
**Tractors are low-fidelity, interactive prototypes** that validate product flows before investing in high-fidelity design. They serve as "visual PRDs" to align stakeholders on functionality and user experience.

### Tractor Principles
- **Intentionally rough** - Must look like obvious prototypes, not polished designs
- **Functional, not beautiful** - Focus on user flow validation, not visual polish
- **Interactive, not static** - Click-through experiences that feel real
- **Fast to create** - Rapid prototyping using reusable components
- **Stakeholder-friendly** - Easy to review and provide feedback
- **Placeholder styling** - Gray backgrounds, dashed borders, basic fonts

## Process

### Phase 1: Understand the Request
- **CRITICAL**: If <70% confident, ask and verify with user before acting
- Identify exactly which screens and/or flow the tractor should show
- Reference any available PRD or context materials
- If no context provided, interview user to understand requirements

### Phase 2: Prototype Composition
- Reference `@shared-knowledge/studio-tractor-kit.pdf` for style guidance
- Combine components into working HTML compositions
- Add interaction logic for click-through functionality
- Include realistic mock data (not Lorem Ipsum!)
- Ensure consistent workspace aesthetic

### Phase 3: Output Generation
- Create complete HTML file with embedded CSS/JS
- Save to project outputs folder
- Generate documentation explaining the flow

## Output Structure

```
projects/[project-name]/output/
├── [feature-name]-tractor.html     # Complete interactive prototype
├── tractor-assets/                 # Supporting files (if needed)
└── tractor-documentation.md        # Flow explanation and notes
```

## When to Create Tractors
- After problem research but before detailed design
- When flows are complex and need validation
- For stakeholder alignment on functionality
- To test user journey assumptions

## Success Metrics
- **Flow validation** - Does the user journey make sense?
- **Stakeholder alignment** - Agreement on functionality?
- **Gap identification** - What requirements were missed?
- **Decision support** - Does this help make product decisions?
