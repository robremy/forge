# Current Architecture

Current architecture is specification-only.

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
