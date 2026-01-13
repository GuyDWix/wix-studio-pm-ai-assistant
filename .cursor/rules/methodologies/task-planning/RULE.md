---
description: "Use when creating task lists, project plans, work breakdowns, or any structured planning requiring phase-level methodology"
alwaysApply: false
---

# Task Planning Methodology

## When to Use
- Creating strategic task lists
- Project planning
- Work breakdown structures
- Complex multi-phase initiatives

## Phase-Level Execution Strategy

For each major phase (e.g., `1.0`, `2.0`), define a Methodology block:

```markdown
- [ ] **X.0 Parent Task Title**
    - **Methodology:**
        - **Context Protocol:** [Single Unified Context | Fresh Instance per Sub-task | Hybrid]
        - **Rationale:** [Why this protocol was chosen]
```

### Context Protocol Definitions

- **Single Unified Context:** One AI instance performs all sub-tasks sequentially
  - *Use for:* Creative or synthesis tasks where context retention is essential

- **Fresh Instance per Sub-task:** Each sub-task executed by new AI instance
  - *Use for:* Engineering or validation tasks to test artifact integrity

- **Hybrid:** Combination - specify which tasks need fresh context
  - *Use for:* Complex phases with mixed creative and technical sub-tasks

## Task Hierarchy Structure

```markdown
- [ ] **X.0 Parent Task Title**
    - **Methodology:**
        - **Context Protocol:** ...
        - **Rationale:** ...
    - [ ] **X.Y Sub-Task Title**
        - **Task Brief:**
            - **LLM Persona:** [Specific role, e.g., "Lead Engineer"]
            - **Required Context:** [List @filename.md files needed]
            - **Instructions:** [Numbered steps]
            - **Output:** [Deliverable description]
```

## Quality Assurance Gates

- **Assumption Validation:** Explicit steps to validate with user
- **Methodology Verification:** Present approach for approval before execution
- **Sample Validation:** Show representative sample for complex transformations
- **Quality Checkpoints:** Logical break points to verify direction

## Implementation Protocol

- **Completion:** When all sub-tasks `[x]`, mark parent as `[x]`
- **Handoff:** Summarize accomplishments before proceeding
- **Living Document:** Keep "Relevant Files/Context" updated
- **Intent-Driven Adaptation:** Proactively suggest updates when goals shift
