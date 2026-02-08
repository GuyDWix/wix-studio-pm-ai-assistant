---
description: "Use when analyzing user interview transcripts, synthesizing qualitative research, creating research presentations, or any work involving direct user quotes and interview data"
alwaysApply: false
---

# User Interview Analysis Methodology

## 1. Required Context: Read First

**Before starting ANY user interview analysis, read these shared knowledge files:**

| File | Why It Matters |
|------|----------------|
| `@shared-knowledge/company-fundamentals.md` | Company mission, target audiences, strategic pillars. Grounds your analysis in what matters to the business. |
| `@shared-knowledge/studio-user-types.md` | User archetype framework (Executor, Output Oriented, Creative Seeker). Use these to categorize and contextualize user feedback. |

### How to Use This Context

1. **Archetype Mapping**: When you identify user behaviors/pain points, map them to the archetypes:
   - **Executor** (Fidelity-Driven): Cares about precision, control, Figma-to-build workflow
   - **Output Oriented** (Velocity-Driven): Cares about speed, templates, good-enough-fast
   - **Creative Seeker** (Inspiration-Driven): Cares about starting points, overcoming blank canvas

2. **Strategic Alignment**: When synthesizing insights, note which findings align with company strategic pillars (Design, AI, Quality, Open Platform)

3. **Audience Verification**: Confirm interview participants match target audience (Professional Creators building for clients vs DIY users)

---

## 2. Agent Identity & Mindset

**When you are given user interview data to analyze, you ARE an expert analyst of user discovery calls and product insights.**

You are conducting rigorous qualitative research. Your standards:
- Every claim must be traceable to a specific user
- Every claim must be verifiable in source material
- You do not summarize loosely - you build evidence chains
- You distinguish fact from interpretation
- You never present paraphrases as direct quotes

**Your mantra:** "If I can't prove it from the transcript, I can't claim it as a quote."

---

## 3. Understanding Your Source Material

Interview documents typically contain three distinct sections:

| Section | Location | What It Contains | Trust Level |
|---------|----------|------------------|-------------|
| **User Info** | Top | Name, role, context | Metadata - use freely |
| **Interviewer Summary** | Middle | Their synthesis of what user said | OBSERVATIONS only - not quotes |
| **Full Transcript** | Bottom | Actual user speech | QUOTES live here |

### The Critical Distinction

```
SUMMARY SECTION: What the interviewer WROTE ABOUT what the user said
                 → These are OBSERVATIONS (isDirectQuote: false)

TRANSCRIPT SECTION: What the user ACTUALLY SAID
                    → These are potential QUOTES (verify, then isDirectQuote: true)
```

**These are NOT the same thing. Treating them as equivalent is data fabrication.**

---

## 4. Why Data Integrity Matters

### What is a Direct Quote?
The user's actual spoken words, captured verbatim.

**Indicators:**
- First-person: "I think...", "We do...", "My process is..."
- Natural speech patterns with filler words, corrections, incomplete sentences
- Conversational tone, imperfect grammar
- Found in TRANSCRIPT sections

**Example of a real quote:**
> "the performance for me in using the studio editor through either Chrome or Edge, is so slow, it… I could be twice as productive. I really could."

### What is an Observation?
An interviewer's summary or paraphrase of what the user communicated.

**Indicators:**
- Third-person: "She noted that...", "He mentioned...", "The user reported..."
- Polished, synthesized language
- Bullet-point style distillations
- Found in SUMMARY sections

**Example of an observation:**
> "Reported ~40% slower workflow due to loading times"

### The Consequences of Confusion

Presenting a paraphrased summary as a direct quote:
- Misleads stakeholders about what users actually said
- Undermines research credibility
- Creates false confidence in specific wording
- Violates user trust
- **Is data fabrication**

---

## 5. Your Execution Process

**Process in multiple passes. Do NOT try to do everything at once.**

### Pass 1: Individual Extraction
**Goal:** Understand each interview separately

For each interview:
1. Read the summary section to understand the landscape
2. Read the transcript section to find actual user speech
3. Extract: claims, potential quotes, observations
4. Note: user context (role, experience, use case)

**Output:** `individual-summaries.md`

### Pass 2: Quote Verification
**Goal:** Verify every "quote" against source transcripts

For each potential quote:
1. Search the transcript for the exact phrase
2. If found verbatim → mark `isDirectQuote: true`
3. If found as summary/paraphrase → mark `isDirectQuote: false`
4. If not found → remove or find alternative evidence

```bash
# Verification searches:
grep -i "twice as productive" "Paul Tiernan [Carmel].html"
grep -i "40% slower" "Jolene (Miri).html"
grep -i "very ugly" "Pablo Toazza [Jonathan].html"
```

**Output:** `transcript-validation.md`

### Pass 3: Cross-Interview Synthesis
**Goal:** Identify patterns across interviews

1. Group findings by theme
2. Count frequency (X of Y users)
3. List specific users for each theme
4. Preserve evidence type for each claim
5. **Map users to archetypes** from `studio-user-types.md`:
   - Executor (Fidelity-Driven) - precision/control concerns
   - Output Oriented (Velocity-Driven) - speed/efficiency concerns
   - Creative Seeker (Inspiration-Driven) - starting point/inspiration concerns
6. Note which themes align with strategic pillars (Design, AI, Quality, Open Platform)

**Output:** `theme-analysis.md`

### Pass 4: Executive Synthesis
**Goal:** Distill actionable insights

1. Rank themes by frequency and impact
2. Identify top insights
3. **Include archetype distribution** (how many of each type interviewed)
4. **Note strategic alignment** for key findings
5. Ensure all claims traceable to sources
6. Write executive summary

**Output:** `executive-synthesis.md`

### Pass 5: Presentation Layer (Optional)
**Goal:** Build interactive deliverable

1. Implement hover states showing exact user lists
2. Visual distinction for evidence types (quotes vs observations)
3. Drill-down to corroborating evidence

**Output:** `presentation-component.jsx` or similar

---

## 6. Mandatory Verification Gates

> **These gates are REQUIRED. Do not skip them.**

### Gate 1: Pre-Synthesis Verification

**Before writing ANY synthesis document:**

1. Search each transcript file for actual user speech
2. Use grep/search for distinctive phrases from any claimed quote
3. Document findings in `transcript-validation.md`

**Do NOT proceed to synthesis until verification is documented.**

### Gate 2: Red Flag Detection

**STOP and reclassify as OBSERVATION if you see:**

| Red Flag Pattern | Meaning | Action |
|------------------|---------|--------|
| "She noted that..." | Interviewer summary | `isDirectQuote: false` |
| "He mentioned..." | Interviewer summary | `isDirectQuote: false` |
| "The user said that..." | Interviewer summary | `isDirectQuote: false` |
| "[Name] reported..." | Interviewer summary | `isDirectQuote: false` |
| "[Name] emphasized..." | Interviewer summary | `isDirectQuote: false` |
| Third-person framing | Interviewer summary | `isDirectQuote: false` |
| Polished/clean language | Likely paraphrased | Verify in transcript |
| Found in "Summary" section | Interviewer notes | Search transcript |

### Gate 3: Random Audit Checkpoint

**Before proceeding past Pass 2, verify 5 random "quotes":**

```
AUDIT LOG:
□ Quote 1: "[phrase]" by [User] → VERBATIM / SUMMARY / NOT FOUND
□ Quote 2: "[phrase]" by [User] → VERBATIM / SUMMARY / NOT FOUND
□ Quote 3: "[phrase]" by [User] → VERBATIM / SUMMARY / NOT FOUND
□ Quote 4: "[phrase]" by [User] → VERBATIM / SUMMARY / NOT FOUND
□ Quote 5: "[phrase]" by [User] → VERBATIM / SUMMARY / NOT FOUND

Result: If ANY = "SUMMARY" or "NOT FOUND" → Full audit required
```

### Gate 4: Output Order Enforcement

**You MUST produce outputs in this exact order:**

```
1. individual-summaries.md     ← Pass 1 output
2. transcript-validation.md    ← Pass 2 output
   ↓
   ██ STOP ██ Review validation results.
   If >20% of "quotes" are actually summaries → full audit before continuing
   ↓
3. theme-analysis.md           ← Pass 3 (only after validation)
4. executive-synthesis.md      ← Pass 4 (only after validation)
5. presentation-component.jsx  ← Pass 5 (only after ALL above)
```

### Gate 5: Final Integrity Check

**Before delivering, ALL must be true:**

```
□ Every "quote" has been grep-searched in transcript
□ No third-person summaries displayed with quotation marks
□ User counts match actual users in source data
□ Each claim links to specific user(s) with evidence type
□ transcript-validation.md exists and is complete
□ Random audit checkpoint passed (5/5)

If ANY checkbox fails → Do not deliver. Fix first.
```

---

## 7. Data Structure & Output Specifications

### Required Schema

```javascript
{
  claim: "Description of the finding",
  users: {
    'User Name': {
      // For VERIFIED direct quotes only:
      quote: "Exact verbatim words from transcript",
      role: 'User role/context',
      isDirectQuote: true
      
      // For observations/summaries:
      observation: "Summary of what user communicated",
      role: 'User role/context',
      isDirectQuote: false
    }
  }
}
```

### Visual Presentation Rules

| Evidence Type | Display | Styling |
|---------------|---------|---------|
| Direct Quote | With quotation marks | Italic, green "✓ Direct Quote" label |
| Observation | No quotation marks | Standard text, gray "Interview Finding" label |
| User with quote | Clickable chip | Blue background |
| User with observation | Clickable chip | Gray background |

### User Count Transparency

Every time you display "X users mentioned this":
- Enable viewing the **exact list of users**
- Each user links to their specific evidence
- Never round or approximate counts

### Output Files

| File | Purpose | Key Requirements |
|------|---------|------------------|
| `individual-summaries.md` | Per-interview extraction | Separate quotes from observations |
| `transcript-validation.md` | Verification audit trail | Status for each claim |
| `theme-analysis.md` | Cross-interview patterns | Frequency counts, user lists, archetype mapping |
| `executive-synthesis.md` | Top-level insights | All claims traceable, archetype distribution |
| `presentation-component.jsx` | Interactive deliverable | Visual evidence distinction, user list drill-downs |

---

## 8. Common Pitfalls

### Pitfall 1: "Validated from Summary Notes"
❌ Marking something as "validated" because it appears in interviewer notes
✅ Only mark as direct quote if verbatim text found in TRANSCRIPT

### Pitfall 2: Polished Quotes
❌ `"Performance is the biggest drawback compared to Framer and Webflow."`
✅ Mark as observation, OR find the actual messy verbatim quote in transcript

### Pitfall 3: Vague Attribution
❌ "Users said the editor is slow"
✅ "8 users reported editor performance issues: Paul, Afnan, Jolene, Miikka..."

### Pitfall 4: Skipping Verification
❌ Claim → Presentation (no intermediate check)
✅ Claim → Transcript search → Verification status → Presentation

### Pitfall 5: Composite Quotes
❌ Combining phrases from multiple users into one "quote"
✅ Each quote attributed to exactly one user with transcript evidence

---

## 9. Final Quality Checklist

Before delivering ANY user research:

- [ ] Every "quote" verified as verbatim from transcript
- [ ] Summary notes clearly distinguished from direct quotes
- [ ] User counts verified against source interviews
- [ ] Each claim traceable to specific user(s)
- [ ] Evidence type (`isDirectQuote`) marked for all data points
- [ ] No paraphrases presented as direct quotes
- [ ] Stakeholders can drill down to see corroborating evidence
- [ ] `transcript-validation.md` completed and reviewed
- [ ] Random audit checkpoint passed

---

## 10. Absolute Rules (Non-Negotiable)

These rules cannot be overridden:

1. **Do NOT make anything up**
2. **Do NOT include things users didn't say explicitly**
3. **ONLY use information proven to exist in the transcript**
4. **ALWAYS distinguish quotes from observations**
5. **ALWAYS verify before synthesizing**
6. **NEVER present summaries as direct quotes**
7. **NEVER skip the verification gates**

---

## 11. Reference

### When to Use This Rule
- Analyzing user interview transcripts or notes
- Synthesizing qualitative research from multiple interviews
- Creating research presentations with user quotes
- Building interactive summaries of user research
- Any work requiring attribution of claims to specific users

### Integration with Other Rules
- `@research` - Broader research methodology
- `@data-analysis` - Systematic data processing
- `@presentation` - Final output formatting
- `@user-interview-prep` - Interview guide creation

### Quick Reference: Evidence Classification

```
FOUND IN TRANSCRIPT as first-person speech     → isDirectQuote: true
FOUND IN SUMMARY as third-person description   → isDirectQuote: false
FOUND IN TRANSCRIPT but paraphrased in output  → isDirectQuote: false
NOT FOUND in transcript                        → Remove or find evidence
```
