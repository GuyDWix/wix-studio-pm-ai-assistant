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

---

## MANDATORY Verification Protocol

> **This section is REQUIRED, not optional. Do not skip these steps.**

### Gate 1: Transcript Search Before Synthesis

Before writing ANY synthesis document, you MUST:

1. **Search each transcript file for actual user speech**
2. **Use grep/search for distinctive phrases** from any claimed quote
3. **Document what you find** in `transcript-validation.md`

```bash
# Example verification searches:
grep -i "twice as productive" "Paul Tiernan [Carmel].html"
grep -i "40% slower" "Jolene (Miri).html"
grep -i "very ugly" "Pablo Toazza [Jonathan].html"
```

### Gate 2: Red Flag Pattern Detection

**STOP and reclassify as OBSERVATION (not quote) if you see these patterns:**

| Pattern in Source | What It Means | Action |
|-------------------|---------------|--------|
| "She noted that..." | Interviewer summary | Mark `isDirectQuote: false` |
| "He mentioned..." | Interviewer summary | Mark `isDirectQuote: false` |
| "The user said that..." | Interviewer summary | Mark `isDirectQuote: false` |
| "[Name] reported..." | Interviewer summary | Mark `isDirectQuote: false` |
| "[Name] emphasized that..." | Interviewer summary | Mark `isDirectQuote: false` |
| Third-person framing | Interviewer summary | Mark `isDirectQuote: false` |
| Polished/clean language | Likely paraphrased | Verify against transcript |
| Found in "Summary" section | Interviewer notes | Search transcript for verbatim |

**Real quotes look like:**
- First person: "I think...", "We do...", "My process..."
- Natural speech: filler words, incomplete sentences, corrections
- Conversational tone with imperfect grammar

### Gate 3: Random Audit Checkpoint

**Before proceeding past synthesis, verify 5 random "quotes":**

1. Pick 5 claims marked as quotes from your analysis
2. Search the actual transcript file for the exact phrase
3. If ANY fail verification, audit ALL quotes before continuing

```
AUDIT LOG:
□ Quote 1: "[phrase]" by [User] → FOUND VERBATIM / FOUND AS SUMMARY / NOT FOUND
□ Quote 2: "[phrase]" by [User] → FOUND VERBATIM / FOUND AS SUMMARY / NOT FOUND
□ Quote 3: "[phrase]" by [User] → FOUND VERBATIM / FOUND AS SUMMARY / NOT FOUND
□ Quote 4: "[phrase]" by [User] → FOUND VERBATIM / FOUND AS SUMMARY / NOT FOUND
□ Quote 5: "[phrase]" by [User] → FOUND VERBATIM / FOUND AS SUMMARY / NOT FOUND

If any = "FOUND AS SUMMARY" or "NOT FOUND" → Full audit required
```

### Gate 4: Gated Output Order

**You MUST produce outputs in this order:**

```
1. individual-summaries.md     ← Extract from each interview
2. transcript-validation.md    ← VERIFY all quotes against transcripts
   ↓
   STOP HERE. Review validation results.
   If >20% of "quotes" are actually summaries → full audit
   ↓
3. theme-analysis.md           ← Only after validation passes
4. executive-synthesis.md      ← Only after validation passes
5. presentation-component.jsx  ← Only after ALL above complete
```

**Do NOT create presentation layer until transcript-validation.md is complete and reviewed.**

### Gate 5: Final Integrity Check

Before delivering ANY user research output, run this check:

```
INTEGRITY CHECK:
□ Every item marked "quote" has been grep-searched in transcript
□ No third-person summaries are presented with quotation marks
□ User counts match actual number of users in source data
□ Each claim links to specific user(s) with evidence type
□ transcript-validation.md exists and documents verification status
□ Random audit checkpoint passed (5/5 verified)
```

**If any checkbox fails → Do not deliver. Fix first.**

---

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

## Sample Analysis Request

Use this template when initiating a user interview analysis project:

```
I need your help as an expert analyst of user discovery calls and product insights.

Our team conducted [NUMBER] user interviews. All information is documented in [FOLDER PATH].
The context includes:
- Interview schedules
- Individual summaries written by team members
- Full transcripts

Each team member's sheet is formatted with:
- User information at the top
- Summary in the middle  
- Full transcript at the bottom

**Analysis Requirements:**

Go over all information diligently and carefully. Process in multiple passes:

1. **PASS 1 - Summary Analysis**: Analyze and synthesize all the different summaries together
2. **PASS 2 - Transcript Review**: Go over the transcripts to ensure nothing important was missed
3. **PASS 3 - Validation**: Verify that transcripts support the analysis and summary

**Critical Rules:**
- Do NOT make anything up
- Do NOT include things users didn't say specifically or explicitly
- ONLY use real information proven to exist in the transcript by users bringing it up
- Distinguish between direct quotes and interviewer observations

**Desired Output:**
A synthesized summary including:
- Main insights from all user talks
- Key themes that emerge across users
- Frequency analysis: which themes are most repeated vs less frequent
- All claims attributed to specific users with evidence type marked

Output analysis to: [OUTPUT FOLDER]

Break this down into several passes so synthesis will be optimal and with the highest quality.
```

## Multi-Pass Analysis Structure

When executing user interview analysis, use this phased approach:

### Pass 1: Individual Processing
- Process each interview separately
- Extract claims, quotes, and observations
- Note user context (role, experience, use case)
- Output: `individual-summaries.md`

### Pass 2: Cross-Interview Synthesis
- Identify recurring themes across interviews
- Count frequency of each theme
- Group users by shared experiences
- Output: `theme-analysis.md`

### Pass 3: Transcript Validation
- For each key claim, search original transcripts
- Verify exact wording exists
- Classify as direct quote or observation
- Output: `transcript-validation.md`

### Pass 4: Executive Synthesis
- Distill top insights
- Rank by frequency and impact
- Ensure all claims traceable to sources
- Output: `executive-synthesis.md`

### Pass 5: Presentation Layer (Optional)
- Build interactive summary
- Implement hover states for user lists
- Visual distinction for evidence types
- Output: `presentation-component.jsx` or similar
