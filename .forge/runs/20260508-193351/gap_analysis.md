# Gap Analysis

Target capability:
Level 1 - Local Kernel

Current limitation:
Forge is documentation-only and has no executable CLI.

Gap:
No runnable Python package exists yet.

Smallest useful improvement:
Build the Level 1 local kernel with status, run, verify, improve, and learn commands.

Acceptance criteria:
- forge status prints current state and maturity.
- forge run --task creates a run folder and required artifacts.
- forge verify runs commands from forge.yml.
- forge improve proposes one gap-based task.
- forge learn --run latest writes lessons.
- pytest passes.

Risk level:
low

Reason for priority:
The maturity model requires a local kernel before any self-improvement loop can run.
