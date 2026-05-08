# Current Architecture

Current architecture is a minimal Python CLI kernel.

Target bootstrap architecture:

```text
CLI
 -> Config loader
 -> State reader
 -> Horizon reader
 -> Gap analyzer
 -> Run context
 -> Test runner
 -> Memory writer
 -> State updater
```

Implemented modules:

```text
src/forge/main.py
src/forge/config.py
src/forge/run_context.py
src/forge/state.py
src/forge/horizon.py
src/forge/gap.py
src/forge/memory.py
src/forge/git_guard.py
src/forge/test_runner.py
```
