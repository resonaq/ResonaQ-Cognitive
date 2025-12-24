# AGENTS — ResonaQ rules for Codex

This repo is a cognitive prompt architecture.

## Always respect layers
- Kernel (single source of truth): kernel/system_snapshot_motorcore.json
- Policy (visibility/format only): policy/talimat.md

## Working style
- Make minimal, safe changes.
- Before editing: list files you will touch.
- After editing: summarize changes + how to verify.

## Bilingual policy (canonical vs rationale)
- English is canonical for architecture/governance/contracts.
- Turkish is allowed for exploration, rationale, design discovery.
- If EN and TR documents conflict, EN wins.
- Use naming convention:
  - docs/*.md = canonical EN
  - docs/*.tr.md = non-canonical TR rationale/commentary
- README may be bilingual, but must not redefine contracts.

## Git discipline
- Prefer one small commit per task.
- Do not refactor unrelated files.
