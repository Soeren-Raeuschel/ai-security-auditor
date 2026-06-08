# AI Governance Documentation

## EU AI Act Classification
- **Risk Level:** Minimal Risk
- **Reason:** Informational tool only — no automated decisions affecting individuals

## Model Usage
- Provider: TBD (Groq / Anthropic)
- Model: TBD
- Purpose: Generating human-readable security reports from scan data

## Auditability
All LLM inputs and outputs are logged to `audit_log.json` with:
- Timestamp
- Input data (headers, SSL results)
- Full model output
- Token usage

## Consistency
Automated tests verify that identical inputs produce equivalent outputs.

## Green Coding
- Scan duration is measured per run
- Token usage is minimized through prompt optimization
- Carbon footprint estimated using GSF SCI Specification
