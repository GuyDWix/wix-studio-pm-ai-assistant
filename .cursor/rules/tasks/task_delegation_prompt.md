# Meta Delegation Prompt (v2)

This is a standardized bootstrapping prompt to orient an expert AI agent within our project and assign it a specific task from our master plan.

---

### How to Use

For any new task, copy the template below, replace `[TASK_NUMBER]` with the specific task you are delegating (e.g., `4.1`), and provide it to a new, fresh LLM instance.

---

### **[COPY AND PASTE BELOW THIS LINE]**

Hello. You are an expert AI agent joining an ongoing project. Your goal is to autonomously execute the next task in our project plan.

Follow this bootstrapping sequence precisely:

Your next task:
<your-next-task>
**[TASK_NUMBER]**.
</your-next-task>

1.  **Understand the Mission:** First, read `[PROJECT_BRIEF]` to internalize the project's high-level goals, core principles, and philosophy.

2.  **Understand the Master Plan:** Next, read `[TASK_LIST]`. This is our single source of truth for all work.

3.  **Identify and Execute Your Task:** Your specific assignment is <your-next-task>
    -   Locate this task in the `task-list.md`.
    -   Adopt the specified `LLM Stance`.
    -   Review the `Required Context`.
    -   Execute the `Instructions` precisely.
    -   Deliver the specified `Output` and nothing else.

Your current assignment is: <your-next-task>

Proceed and let me know once your'e finished.