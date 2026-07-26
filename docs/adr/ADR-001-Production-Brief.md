# ADR-001 — Production Brief as the Source of Creative Truth
## The canonical representation of a creative project.
Status:
Accepted

Date:
2026-07

---

## Context

Traditional AI image workflows begin with prompt engineering.

This tightly couples creative thinking to the syntax and capabilities of a specific AI model.

VizClick aims to be model-agnostic.

---

## Decision

VizClick introduces the Production Brief as the canonical representation of creative intent.

The Production Brief contains structured creative information independent of any AI model.

Prompts are compiled outputs, not authoring inputs.

---

## Consequences

Benefits

• Model-independent architecture

• Easier localization

• AI provider independence

• Rich validation

• Future compatibility with video and 3D workflows

Tradeoffs

• Additional abstraction layer

• Compiler required before generation

---

## Pipeline

Creative Vision

↓

Production Brief

↓

Scene Graph

↓

Compiler

↓

Prompt

↓

AI Model