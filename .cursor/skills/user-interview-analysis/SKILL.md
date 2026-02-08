---
name: user-interview-analysis
description: Analyze user interview transcripts and synthesize insights with rigorous data integrity. Use when analyzing user calls, creating research summaries, building interview presentations, or when the user references interview transcripts, user research, or discovery calls.
---

# User Interview Analysis

Synthesize user interview data into actionable insights while maintaining rigorous data integrity. The core principle: **never present paraphrased summaries as direct quotes**.

## Quick Start

When given interview data:

1. **Read the methodology rule** at `.cursor/rules/methodologies/user-interview-analysis/RULE.md`
2. **Identify source types**: Transcripts (verbatim) vs Summary notes (paraphrased)
3. **Execute multi-pass analysis** (see workflow below)
4. **Output to project's `/output` folder**

## Critical Data Integrity Rules

### Direct Quotes vs Observations

| Type | Markers | Can Use Quotation Marks? |
|------|---------|--------------------------|
| **Direct Quote** | First-person ("I think..."), natural speech, filler words | ✅ Yes |
| **Observation** | Third-person ("He said...", "She noted..."), polished language | ❌ No |

### Verification Process

For every "quote" in output:
```
1. SEARCH transcript for exact phrase
2. IF found verbatim → isDirectQuote: true
3. IF found as "said that/noted/mentioned" → isDirectQuote: false (observation)
4. IF not found → remove or find alternative evidence
```

### Data Structure

```javascript
{
  claim: "Finding description",
  users: {
    'User Name': {
      quote: "Exact verbatim words",      // OR
      observation: "Summary of what user said",
      role: 'User context',
      isDirectQuote: true  // or false
    }
  }
}
```

## Multi-Pass Analysis Workflow

### Pass 1: Individual Extraction
For each interview:
- Extract key insights from summary section
- Note user context (role, experience, segment)
- Flag potential direct quotes for verification

**Output**: `individual-summaries.md`

### Pass 2: Transcript Verification
For each flagged quote:
- Search transcript for exact wording
- Classify as direct quote or observation
- Document evidence source

**Output**: `transcript-validation.md`

### Pass 3: Theme Synthesis
- Group findings by theme
- Count frequency (X of Y users)
- List specific users per theme
- Identify patterns and contradictions

**Output**: `theme-analysis.md`

### Pass 4: Executive Synthesis
- Top 3-5 critical insights
- User archetype patterns
- Priority recommendations
- All claims traceable to sources

**Output**: `executive-synthesis.md`

### Pass 5: Interactive Presentation (Optional)
- Hover states for user lists
- Evidence type visual distinction
- Drill-down to corroborating data

**Output**: `presentation-component.jsx`

## Output Templates

### Theme Entry
```markdown
## [Theme Name]
**Frequency**: X of Y users (list: User1, User2, User3...)
**Severity/Priority**: [High/Medium/Low]

### Evidence
- **User1** (Role): [Quote or Observation]
- **User2** (Role): [Quote or Observation]
```

### Insight Card (for presentations)
```javascript
{
  title: "Insight title",
  description: "Brief explanation",
  users: { /* user evidence structure */ },
  severity: 85  // 0-100 scale
}
```

## Quality Checklist

Before delivering:
- [ ] Every "quote" verified verbatim from transcript
- [ ] Observations clearly distinguished (no quotation marks)
- [ ] User counts verifiable (hoverable/expandable lists)
- [ ] Each claim has user attribution
- [ ] Evidence type marked (`isDirectQuote: true/false`)
- [ ] No composite or polished quotes

## Common Pitfalls

| Pitfall | Wrong | Right |
|---------|-------|-------|
| Summary as quote | `"Performance is biggest drawback"` | Observation: Cited performance as biggest drawback |
| Vague attribution | "Users said..." | "8 users reported: Paul, Afnan, Jolene..." |
| Missing evidence chain | Claim → Output | Claim → Transcript search → Classification → Output |

## Integration

- **Methodology details**: See `.cursor/rules/methodologies/user-interview-analysis/RULE.md`
- **Research process**: Use with `@research` methodology for broader context
- **Data analysis**: Use with `@data-analysis` for systematic processing

## File Structure

```
projects/[project-name]/
├── context/
│   └── [interview-files]/     # Source transcripts/notes
└── output/
    ├── individual-summaries.md
    ├── transcript-validation.md
    ├── theme-analysis.md
    ├── executive-synthesis.md
    └── presentation-component.jsx  # Optional
```
