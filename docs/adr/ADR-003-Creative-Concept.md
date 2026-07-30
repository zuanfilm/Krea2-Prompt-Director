# ADR-003 — Creative Knowledge Ecology (CKE)

> **The renderer-independent knowledge system that stores reusable creative concepts.**

**Status:** Accepted

---

# Context

As VizClick evolved beyond prompt generation, it became necessary to
separate reusable creative knowledge from individual creative works.
The Creative Knowledge Ecology represents accumulated reusable creative
knowledge.

It intentionally does not limit creativity.

Creators may always introduce ideas beyond the current knowledge base
through Custom Creative Intent.

Creative ideas such as:

- Golden Hour
- Editorial Fashion
- Marble
- Rule of Thirds
- Soft Diffused Lighting

should not be recreated for every project.

Instead, they should exist as reusable knowledge that can be shared,
combined, and interpreted consistently across every creative domain.

This requires a centralized knowledge system independent from renderers,
creative briefs, and individual projects.

---

# Decision

VizClick adopts the **Creative Knowledge Ecology (CKE)** as the canonical
repository of reusable creative knowledge.

The Creative Knowledge Ecology stores immutable Creative Concepts and the
semantic relationships between them.

The CKE is renderer-independent.

It does not contain prompts, renderer syntax, optimization rules, or
project-specific information.

Instead, it provides the reusable vocabulary from which creative intent
is composed.

---

# Responsibilities

The Creative Knowledge Ecology is responsible for:

- storing Creative Concepts
- organizing concepts into domains
- maintaining semantic relationships
- supporting concept discovery
- enabling concept reuse
- preserving renderer independence

The CKE is a knowledge system.

It is not a project.

It is not a scene.

It is not a renderer.

---

# Creative Concepts

Creative Concepts are the smallest reusable units of creative knowledge.

Each Creative Concept represents a single creative idea.

Examples include:

- Golden Hour
- Marble
- Luxury
- Rule of Thirds
- Dynamic Motion Blur
- Chiaroscuro
- Rain

Creative Concepts remain immutable.

Projects reference Creative Concepts rather than duplicating them.

---

# Relationships

Creative Concepts gain additional meaning through semantic relationships.

Examples include:

- supports
- combines_with
- avoids
- influences
- commonly_used_in

These relationships describe creative practice rather than renderer
behavior.

For example:

Golden Hour

supports → Warm Atmosphere

combines_with → Rim Lighting

avoids → Flat Lighting

influences → Nostalgia

Relationships remain renderer-independent.

---

# Architecture

```text
Creative Knowledge Ecology (CKE)
                │
                ▼
Creative Concepts
                │
                ▼
Creative Relationships
                │
                ▼
Creative Briefs
                │
                ▼
Creative Representation Layer (CRL)
                │
                ▼
Production Brief
                │
                ▼
Renderer Adapter
                │
                ▼
Rendered Output
```

---

# Design Principles

## Immutable Knowledge

Creative Concepts are immutable.

They represent stable creative knowledge rather than project-specific
decisions.

---

## Renderer Independence

Creative Concepts never contain:

- prompt syntax
- keyword weighting
- renderer parameters
- optimization techniques

These belong exclusively to Renderer Adapters.

---

## Reusability

Creative Concepts are intended to be reused across unlimited projects.

A single concept should be defined once and referenced many times.

---

## Composability

Complex creative intent emerges from combinations of multiple Creative
Concepts.

No concept assumes a specific renderer, subject, or project.

---

## Extensibility

The Creative Knowledge Ecology is designed to grow continuously.

New concepts can be added without changing the architecture.

Existing concepts remain stable.

---

# Consequences

## Positive

- Reusable creative knowledge
- Renderer independence
- Consistent semantics
- Reduced duplication
- Explainable creative reasoning
- Long-term scalability

## Trade-offs

- Requires knowledge curation
- Requires semantic relationship management
- Introduces an additional abstraction layer

These trade-offs are accepted because they produce a reusable,
future-proof creative knowledge system.

---

# Philosophy

Creative knowledge should exist independently of projects.

Projects compose knowledge.

Renderers translate knowledge.

Knowledge itself remains unchanged.

---

# Guiding Principle

> Define knowledge once. Reuse it everywhere.