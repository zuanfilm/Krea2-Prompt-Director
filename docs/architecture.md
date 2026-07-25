# VizClick Architecture

> **The Scene Graph is the source of truth. Prompts are compiled artifacts.**

---

# 1. Overview

VizClick is a visual intelligence framework for AI image generation.

Unlike traditional prompting tools, VizClick does not consider prompts to be the primary creative artifact.

Instead, creators build structured **Production Briefs** which are internally represented as a **Scene Graph**. AI prompts are generated from this representation through model-specific compilation.

This architecture separates **creative thinking** from **AI syntax**, allowing the same creative vision to be exported to multiple AI models without rewriting prompts.

---

# 2. System Philosophy

VizClick is built around one fundamental principle:

> **Artists shouldn't have to learn how AI thinks. AI should learn how artists think.**

Creative professionals think in:

- Subjects
- Composition
- Lighting
- Camera
- Fashion
- Emotion
- Story
- Environment

They do **not** naturally think in prompt syntax.

VizClick translates creative language into optimized prompts while preserving the user's original vision.

---

# 3. Fundamental Architecture Principle

> **The Scene Graph is the canonical representation of creative intent.**

Everything inside VizClick either:

- Creates information for the Scene Graph
- Enriches the Scene Graph
- Validates the Scene Graph
- Compiles the Scene Graph

No subsystem owns creative information except the Scene Graph.

Prompts are generated outputs—not the source of truth.

---

# 4. High-Level Architecture

```
                    USER

                      │
                      ▼

              Interface Layer

                      │
                      ▼

          VizClick Scene Graph
                 (VCSG)

                      │

        ┌─────────────┴─────────────┐

        ▼                           ▼

 VizClick Knowledge Base      VizClick Asset Registry
         (VCKB)                     (VCAR)

        └─────────────┬─────────────┘
                      │
                      ▼

     VizClick Intelligence Framework
                 (VCIF)

                      │
                      ▼

      VizClick Creative Engine
                 (VCEC)

                      │
                      ▼

      VizClick Export Profiles
                 (VCEP)

                      │
                      ▼

         Compiled Model Prompt

                      │
                      ▼

                AI Image Model
```

---

# 5. Core Systems

## VCSG — VizClick Scene Graph

The Scene Graph is the heart of VizClick.

It stores every creative decision independently from any AI model.

Examples include:

- Subjects
- Relationships
- Camera
- Lighting
- Environment
- Wardrobe
- Color Palette
- Style
- Composition
- Director Notes
- Character References

Every other subsystem reads from or enriches the Scene Graph.

---

## VCKB — VizClick Knowledge Base

The Knowledge Base provides structured visual knowledge.

Examples:

- Fashion
- Photography
- Cinema
- Architecture
- Art History
- Lighting
- Lens characteristics
- Camera language
- Materials
- Color theory

The Knowledge Base never modifies the Scene Graph directly.

It provides recommendations and contextual information.

---

## VCAR — VizClick Asset Registry

Stores reusable creative assets.

Examples:

- Character presets
- Style presets
- Wardrobe libraries
- Lighting setups
- Camera rigs
- Scene templates
- Color palettes
- User favorites

Assets are reusable building blocks.

---

## VCIF — VizClick Intelligence Framework

Provides AI-assisted creative guidance.

Responsibilities include:

- Scene Inspector
- Consistency validation
- Creative recommendations
- Missing information detection
- Style suggestions
- Composition analysis
- AI provider integration

The Intelligence Framework assists creators but never replaces creative decisions.

---

## VCEC — VizClick Creative Engine

The Creative Engine transforms creative structure into model-ready outputs.

Responsibilities include:

- Scene interpretation
- Prompt compilation
- Prompt weighting
- Syntax optimization
- Model adaptation
- Token ordering
- Prompt cleanup

Internally, the Creative Engine may contain multiple compilers.

Each supported AI model can have its own compilation strategy.

---

## VCEP — VizClick Export Profiles

Every AI model speaks a different visual language.

Export Profiles adapt the compiled prompt to each destination.

Examples:

- Krea
- FLUX
- Ideogram
- Qwen Image
- Midjourney
- Stable Diffusion
- Future video models
- Future 3D systems

The Scene Graph remains unchanged.

Only the exported representation changes.

---

## VCLF — VizClick Localization Framework

Separates interface language from prompt language.

Responsibilities include:

- UI localization
- Terminology translation
- Prompt language selection
- Regional formatting
- Future multilingual documentation

Creative information remains language-independent whenever possible.

---

# 6. Data Flow

```
Creative Vision

        │

        ▼

Production Brief

        │

        ▼

Scene Graph (VCSG)

        │

        ▼

Knowledge + Assets + Intelligence

        │

        ▼

Creative Engine (VCEC)

        │

        ▼

Export Profile (VCEP)

        │

        ▼

Compiled Prompt

        │

        ▼

AI Model

        │

        ▼

Generated Image
```

---

# 7. Separation of Responsibilities

| System | Responsibility |
|---------|----------------|
| UI | User interaction |
| VCSG | Creative structure (source of truth) |
| VCKB | Visual knowledge |
| VCAR | Reusable creative assets |
| VCIF | AI-assisted creative intelligence |
| VCEC | Prompt compilation and optimization |
| VCEP | Model-specific adaptation |
| VCLF | Localization and language management |

---

# 8. ComfyUI Integration Philosophy

VizClick does not replace ComfyUI.

VizClick complements ComfyUI.

```
ComfyUI

      +

VizClick

      ↓

Creative Intelligence Layer
```

### ComfyUI manages

- Nodes
- Models
- Samplers
- Images
- Execution
- Workflow graph

### VizClick manages

- Creative planning
- Production Briefs
- Scene organization
- Visual direction
- Prompt intelligence
- Localization
- Multi-model exports

Together they provide a complete creative workflow.

---

# 9. Extension System

VizClick is designed as an extensible platform.

Future modules may include:

- Character Brief System
- Storyboard Builder
- Video Scene Compiler
- Architecture Toolkit
- Product Photography Toolkit
- Fashion Toolkit
- Game Art Toolkit
- Asset Marketplace
- Community Presets
- Cloud Synchronization

Every extension communicates through the Scene Graph.

---

# 10. Future Compatibility

VizClick is intentionally model-agnostic.

Today:

```
VizClick

↓

FLUX
Krea
Ideogram
Qwen Image
Stable Diffusion
```

Tomorrow:

```
VizClick

↓

Video Models

↓

3D Scene Generators

↓

Game Engines

↓

Virtual Production

↓

Robotics

↓

Future Creative AI Systems
```

As AI evolves, the Scene Graph remains stable.

Only the compilers and export profiles evolve.

---

# Architecture Philosophy

VizClick is not a prompt generator.

It is not a model wrapper.

It is not tied to any AI provider.

VizClick is a visual intelligence platform where creators express ideas naturally through structured creative thinking.

The Scene Graph is the source of truth.

Everything else is a translation.
