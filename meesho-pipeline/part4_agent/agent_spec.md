# Agent Specification

- **Goal**: Keep Meesho category managers informed of any category whose MoM revenue moves beyond the 8% threshold.
- **Tools**: `validate_feed`, `mom_growth`, `is_flagged`.
- **Memory/State**: Stores historical monthly category revenue values.
- **Planner**: Sequences execution from feed validation to flagging and alert drafting.
- **Feedback Loop**: Requires human approval before any alert is sent out.