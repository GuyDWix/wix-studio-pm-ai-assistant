# Prioritization Frameworks

*Frameworks for feature ranking, resource allocation, and decision making*

## RICE Framework (Intercom)
**Purpose**: Score features based on multiple factors

**Formula**: `(Reach × Impact × Confidence) ÷ Effort = RICE Score`

**Components**:
- **Reach**: How many people will be affected (per time period)
- **Impact**: How much will it impact each person (1-3 scale)
- **Confidence**: How certain are you about your estimates (percentage)
- **Effort**: How much work is required (person-months)

**Best Practice**: Use relative scoring rather than precise numbers

**Wix Studio Application**:
- **Reach**: Partner accounts vs Self Creator accounts affected
- **Impact**: Effect on conversion, retention, or satisfaction
- **Confidence**: Based on user research and data quality
- **Effort**: Development complexity considering platform architecture

**Example Studio RICE Scoring**:
```
Feature: Advanced CSS Editor
Reach: 15,000 Partner accounts (monthly)
Impact: 2.5 (significant workflow improvement)
Confidence: 80% (strong user research)
Effort: 4 person-months
RICE Score = (15,000 × 2.5 × 0.8) ÷ 4 = 7,500
```

---

## ICE Framework
**Purpose**: Quick prioritization for early-stage products

**Components**:
- **Impact**: How much will this move the needle?
- **Confidence**: How sure are we this will work?
- **Ease**: How easy is this to implement?

**Scoring**: 1-10 scale for each component
**Formula**: `(Impact + Confidence + Ease) ÷ 3`

**When to Use**:
- Early-stage features with limited data
- Rapid brainstorming sessions
- Initial feature filtering before detailed analysis

**Studio ICE Examples**:
```
AI Design Assistant:
Impact: 9 (major workflow enhancement)
Confidence: 6 (AI features are promising but uncertain)
Ease: 4 (complex AI integration)
ICE Score = (9 + 6 + 4) ÷ 3 = 6.3

Template Library Expansion:
Impact: 7 (moderate user value)
Confidence: 9 (proven demand)
Ease: 8 (straightforward implementation)
ICE Score = (7 + 9 + 8) ÷ 3 = 8.0
```

---

## Opportunity Scoring (Dan Olsen)
**Purpose**: Prioritize opportunities based on importance vs satisfaction gap

**Process**:
1. Survey customers on opportunity importance (1-5 scale)
2. Survey current satisfaction with existing solutions (1-5 scale)
3. Calculate opportunity score: `Importance + (Importance - Satisfaction)`
4. Focus on highest-scoring opportunities

**Visual**: Plot on Importance vs Satisfaction matrix

**Quadrants**:
- **High Importance, Low Satisfaction**: Primary opportunities
- **High Importance, High Satisfaction**: Maintain excellence
- **Low Importance, High Satisfaction**: Potential over-investment
- **Low Importance, Low Satisfaction**: Ignore or eliminate

**Studio Opportunity Examples**:
```
Site Performance Optimization:
Importance: 4.8/5 (critical for Partners)
Satisfaction: 2.1/5 (current pain point)
Opportunity Score = 4.8 + (4.8 - 2.1) = 7.5

Template Customization:
Importance: 4.2/5 (valuable for creativity)
Satisfaction: 3.8/5 (decent current state)
Opportunity Score = 4.2 + (4.2 - 3.8) = 4.6
```

---

## Value vs Effort Matrix (2x2)
**Purpose**: Quick visual prioritization

**Quadrants**:
- **High Value, Low Effort**: Quick wins (do first)
- **High Value, High Effort**: Major projects (plan carefully)
- **Low Value, Low Effort**: Fill-ins (do if capacity)
- **Low Value, High Effort**: Avoid

**Implementation Tips**:
- Use relative positioning, not absolute numbers
- Consider both user value and business value
- Factor in technical debt and platform health
- Review placement with cross-functional team

**Studio Matrix Example**:
```
Quick Wins (High Value, Low Effort):
- Keyboard shortcuts for common actions
- Export format additions
- Minor UI polish improvements

Major Projects (High Value, High Effort):
- Advanced animation editor
- Multi-site management dashboard
- Collaborative editing features

Fill-ins (Low Value, Low Effort):
- Additional font options
- Color palette expansions
- Tutorial video updates

Avoid (Low Value, High Effort):
- Complex integrations with niche tools
- Over-engineered customization options
- Features that duplicate existing functionality
```

---

## WSJF (Weighted Shortest Job First)
**Purpose**: Maximize economic benefit by sequencing work

**Formula**: `Cost of Delay ÷ Job Duration = WSJF Score`

**Cost of Delay Components**:
- **User/Business Value**: Direct value delivery
- **Time Criticality**: Urgency of delivery
- **Risk Reduction**: Technical or market risk mitigation

**Best For**: Large organizations with multiple competing priorities

**Studio Adaptation**:
- Factor in competitive pressure (design tool landscape)
- Consider platform architecture dependencies
- Weight Partner revenue impact vs Self Creator growth

---

## Kano Model
**Purpose**: Categorize features by user satisfaction impact

**Feature Categories**:
- **Basic Needs**: Must-haves (absence causes dissatisfaction)
- **Performance Needs**: More is better (linear satisfaction)
- **Excitement Needs**: Delighters (unexpected value)
- **Indifferent**: Users don't care
- **Reverse**: Users actively dislike

**Application Process**:
1. Survey users with functional/dysfunctional question pairs
2. Categorize each feature based on responses
3. Prioritize Basic Needs, then Performance, then Excitement

**Studio Kano Examples**:
- **Basic**: Site loading speed, reliability, saving work
- **Performance**: Design flexibility, template quality, publishing speed
- **Excitement**: AI design suggestions, automatic responsive layouts
- **Indifferent**: Advanced export options for most users
- **Reverse**: Overly complex interfaces, forced onboarding

---

## Prioritization Framework Selection Guide

### **Choose Based on Context**:

| Situation | Best Framework | Why |
|-----------|----------------|-----|
| **Early stage product** | ICE | Quick decisions with limited data |
| **Established product** | RICE | Comprehensive analysis with good data |
| **User research available** | Opportunity Scoring | Leverage direct user feedback |
| **Need visual simplicity** | Value vs Effort | Easy stakeholder communication |
| **Multiple stakeholders** | WSJF | Economic focus for alignment |
| **Feature satisfaction focus** | Kano Model | Understand user satisfaction drivers |

### **Framework Combinations**:
- **Comprehensive Stack**: Opportunity Scoring → RICE → Value/Effort
- **Quick Decision Stack**: ICE → Value/Effort
- **User-Centric Stack**: Kano → Opportunity Scoring → RICE

### **Common Mistakes to Avoid**:
- **Over-precision**: Don't spend more time scoring than building
- **Analysis paralysis**: Pick a framework and move forward
- **Ignoring qualitative factors**: Numbers don't tell the whole story
- **Infrequent re-evaluation**: Priorities change, scores should too

---

## Prioritization Best Practices

### **Scoring Guidelines**:
1. **Involve the team**: Get diverse perspectives in scoring
2. **Use relative scoring**: Compare features to each other
3. **Document assumptions**: Record reasoning for future reference
4. **Regular reviews**: Update scores as you learn more
5. **Balance quantitative and qualitative**: Numbers inform, don't dictate

### **Studio-Specific Considerations**:
- **Dual audience impact**: Consider Partner vs Self Creator differently
- **Platform dependencies**: Some features unlock others
- **Competitive dynamics**: Design tool space moves quickly
- **Technical debt**: Balance new features with platform health
- **Resource constraints**: Factor in current team capabilities

### **Communication Tips**:
- **Show your work**: Explain scoring rationale to stakeholders
- **Highlight trade-offs**: Make opportunity costs explicit
- **Use visuals**: Charts and matrices aid understanding
- **Regular updates**: Keep stakeholders informed of priority changes

---

*💡 The best prioritization framework is the one your team uses consistently. Start simple with ICE or Value/Effort, then add complexity as needed. Always combine quantitative scoring with qualitative judgment.* 