---
description: Delegate a task to a fresh AI instance with proper context bootstrapping
---

Prepare a task delegation prompt for a fresh AI instance.

Ask the user for:
- Task number to delegate
- Project brief location (or help locate it)
- Task list location (or help locate it)

Then generate a bootstrapping prompt:

```
Hello. You are an expert AI agent joining an ongoing project.

Your next task: **[TASK_NUMBER]**

Bootstrapping sequence:
1. Read `[PROJECT_BRIEF]` to understand goals and principles
2. Read `[TASK_LIST]` - our single source of truth
3. Execute your task:
   - Locate in task-list.md
   - Adopt the specified LLM Persona
   - Review Required Context
   - Execute Instructions precisely
   - Deliver specified Output

Proceed and let me know once finished.
```

**User's request**: {{input}}
