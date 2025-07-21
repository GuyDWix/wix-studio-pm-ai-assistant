# PM AI Assistant - Wix Studio

A structured framework system for product management work at Wix Studio. Combines task rules, knowledge base, and workflows to enhance AI-assisted PM activities.

## Components

- **Task Rules**: Invoke specific workflows by tagging (`@task-prd-writer`, `@task-research-orchestrator`)
- **Knowledge Base**: Wix Studio context, PM frameworks, and company insights
- **Project System**: Reference previous work and build context (`@projects/feature-x/output/`)
- **Framework Collection**: Strategic, prioritization, development, and metrics methodologies

## Capabilities

- **Product Discovery**: User research, opportunity identification, competitive analysis
- **Requirements & Planning**: PRD writing, feature prioritization (RICE, ICE), roadmap planning  
- **Strategic Decision-Making**: Framework-driven analysis, risk assessment, trade-off evaluation
- **Research & Analysis**: Automated synthesis, insight generation, stakeholder reporting
- **Execution Support**: Task management, progress tracking, stakeholder alignment

## Usage

### Basic Pattern
1. Tag rules for specific workflows: `@task-prd-writer`, `@task-research-orchestrator`
2. Add context materials to `projects/[name]/context/` for better results
3. Reference previous work: `@projects/feature-x/output/` to build on existing insights
4. Ask the AI to break plans into tasks with `@task-create-task-list` to make sure it works methodically and is not going stray.
5. Let the AI suggest approaches when exploring options

### Workflows

| Input | Output |
|-------|--------|
| `"Use @task-research-orchestrator for [topic]"` | 3-phase research with structured findings |
| `"Apply @task-prd-writer for [feature]"` | Complete PRD with requirements gathering |
| `"@task-create-task-list for [initiative]"` | Hierarchical task breakdown with quality checkpoints |
| `"@task-complex-data-analysis for [data work]"` | Systematic data analysis with validation steps |
| `"Reference @shared-knowledge/frameworks/ to analyze X"` | Framework-guided analysis |

## Contents

- **Task Rules**: `@task-prd-writer`, `@task-research-orchestrator`, `@task-create-task-list`, `@task-complex-data-analysis`
- **Knowledge Base**: Wix Studio context, user personas, PM frameworks  
- **PM Frameworks**: Strategic, Prioritization, Development, Metrics methodologies

## Getting Started

Describe your PM challenge. Tag specific rules and reference context for better results. 