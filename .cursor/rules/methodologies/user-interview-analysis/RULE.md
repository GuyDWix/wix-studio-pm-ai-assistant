---
description: "Use when analyzing user interview transcripts, synthesizing qualitative research, creating research presentations, or any work involving direct user quotes and interview data"
alwaysApply: false
---

# User Interview Analysis Methodology

## When to Use
- Analyzing user interview transcripts or notes
- Synthesizing qualitative research from multiple interviews
- Creating research presentations with user quotes
- Building interactive summaries of user research
- Any work requiring attribution of claims to specific users

## Critical Principle: Data Integrity

**The most important rule in user interview analysis is distinguishing between DIRECT QUOTES and OBSERVATIONS.**

### What is a Direct Quote?
A **direct quote** is the user's actual spoken words, captured verbatim from transcript or recording.

**Indicators of direct quotes:**
- First-person language ("I think...", "We do...", "My process is...")
- Conversational tone with natural speech patterns
- May include filler words, corrections, incomplete sentences
- Found in transcript sections, not summary sections

**Example:**
> "the performance for me in using the studio editor through either Chrome or Edge, is so slow, it… I could be twice as productive. I really could."

### What is an Observation/Finding?
An **observation** is an interviewer's summary or paraphrase of what the user communicated.

**Indicators of observations:**
- Third-person framing ("He said that...", "She noted...", "The user mentioned...")
- Polished, synthesized language
- Found in summary sections or notes
- Bullet-point style distillations

**Example:**
> "Reported ~40% slower workflow due to loading times" (interviewer note about what user said)

### Why This Matters
Presenting a paraphrased summary as a direct quote is **data fabrication**. It:
- Misleads stakeholders about what users actually said
- Undermines research credibility
- Creates false confidence in specific wording
- Violates user trust

## Verification Process

### Step 1: Identify All Claims
Extract every claim that will appear in the final output:
- Pain points attributed to users
- Feature requests with user names
- Workflow descriptions
- Quotes displayed in presentations

### Step 2: Classify Evidence Type
For each claim, search the source transcript for the **exact wording**:

```
SEARCH: "[distinctive phrase from claimed quote]"
LOCATION: [user]'s transcript file

RESULT:
- FOUND VERBATIM → Mark as isDirectQuote: true
- FOUND AS SUMMARY (with "said that", "noted", "mentioned") → Mark as isDirectQuote: false
- NOT FOUND → Remove or find alternative evidence
```

### Step 3: Source Documentation
Every claim in the final output must have:
- **User attribution**: Who said/reported this
- **Evidence type**: Direct quote OR observation
- **Source reference**: Which transcript/interview

## Data Structure for Transparent Research

### Recommended Schema

```javascript
{
  claim: "Description of the finding",
  users: {
    'User Name': {
      // For verified direct quotes:
      quote: "Exact verbatim words from transcript",
      role: 'User role/context',
      isDirectQuote: true
      
      // OR for observations/summaries:
      observation: "Summary of what user communicated",
      role: 'User role/context',
      isDirectQuote: false
    }
  }
}
```

### Visual Differentiation
When presenting research:
- **Direct quotes**: Use quotation marks, italic styling, green "✓ Direct Quote" label
- **Observations**: No quotation marks, standard text, gray "Interview Finding" label
- **User chips**: Blue background for users with direct quotes, gray for observations

## Synthesis Artifacts

### Required Outputs

1. **Individual Summaries** (`individual-summaries.md`)
   - One section per interview
   - Clearly separate transcript quotes from interviewer notes
   - Include user context (role, experience level)

2. **Theme Analysis** (`theme-analysis.md`)
   - Group findings by theme
   - Show frequency counts (X of Y users)
   - List specific users for each theme

3. **Transcript Validation** (`transcript-validation.md`)
   - Document verification status of each key claim
   - Mark as: ✅ VALIDATED (with transcript evidence) | ⚠️ PARTIAL | 📝 NOTES ONLY
   - **Critical**: "VALIDATED (from summary notes)" is NOT the same as a direct quote

4. **Executive Synthesis** (`executive-synthesis.md`)
   - Top-level findings
   - All claims traceable to source interviews
   - User counts verifiable against individual summaries

5. **Interactive Presentation** (optional)
   - Hover states showing exact user lists
   - Click-through to corroborating evidence
   - Visual distinction between evidence types

## Presentation Best Practices

### User Count Transparency
Every time you display "X users mentioned this":
- Enable viewing the **exact list of users**
- Each user should link to their specific evidence
- Never round or approximate counts

### Quote Display Rules
1. Only use quotation marks for verified verbatim quotes
2. Always show attribution (user name + role)
3. Indicate evidence type visually
4. Enable drill-down to source

### Never Fabricate or Extrapolate
- Don't create composite quotes from multiple users
- Don't polish or clean up verbatim quotes
- Don't attribute generic findings to specific users without evidence
- Don't infer what users "would say" based on patterns

## Quality Checklist

Before delivering user research:

- [ ] Every "quote" verified as verbatim from transcript
- [ ] Summary notes clearly distinguished from direct quotes
- [ ] User counts verified against source interviews
- [ ] Each claim traceable to specific user(s)
- [ ] Evidence type marked for all data points
- [ ] No paraphrases presented as direct quotes
- [ ] Stakeholders can drill down to see corroborating evidence

## Common Pitfalls to Avoid

### Pitfall 1: "Validated from Summary Notes"
❌ Marking something as "validated" because it appears in interviewer notes
✅ Only mark as direct quote if verbatim text found in transcript

### Pitfall 2: Polished Quotes
❌ "Performance is the biggest drawback compared to Framer and Webflow."
✅ "Performance is the biggest drawback" (observation from notes) or actual verbatim quote with natural speech patterns

### Pitfall 3: Aggregated Attribution
❌ "Users said the editor is slow" (vague)
✅ "8 users reported editor performance issues: Paul, Afnan, Jolene, Miikka..." (specific)

### Pitfall 4: Missing Evidence Chain
❌ Claim → Presentation (no intermediate verification)
✅ Claim → Transcript search → Verification status → Presentation with evidence type

## Integration

- Use with `@research` for broader research methodology
- Use with `@data-analysis` for systematic processing of interview data
- Use with `@presentation` for final output formatting
- Reference `@user-interview-prep` for interview guide creation

## Example Workflow

```
1. COLLECT: Gather all interview transcripts and notes
2. EXTRACT: Identify claims, quotes, and findings from each
3. VERIFY: Search transcripts for exact wording of each "quote"
4. CLASSIFY: Mark each as direct quote or observation
5. STRUCTURE: Organize with proper attribution and evidence type
6. SYNTHESIZE: Create themes while preserving source links
7. PRESENT: Build output with transparent evidence chain
8. VALIDATE: Run quality checklist before delivery
```
