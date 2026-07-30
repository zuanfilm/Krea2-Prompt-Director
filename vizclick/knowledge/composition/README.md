# Composition

> **The creative domain that describes how visual elements are organized and spatially arranged within a Creative Representation.**

Composition is one of the core domains of the **Creative Knowledge Ecology (CKE)**.

Rather than describing renderer-specific framing tools, camera controls,
or layout APIs, Composition represents reusable creative knowledge about
how visual elements are organized to communicate meaning.

Composition shapes how viewers perceive, interpret, and emotionally
engage with a Creative Representation.

Composition concepts are renderer-independent.

They describe **creative organization and spatial intent** rather than
technical implementation.

---

# Purpose

The Composition domain provides reusable Creative Concepts that organize
visual information within a Creative Representation.

Composition influences:

- Visual hierarchy
- Balance
- Focus
- Attention
- Depth
- Rhythm
- Tension
- Symmetry
- Scale
- Spatial relationships
- Reading flow
- Storytelling clarity

These concepts become building blocks for Creative Briefs and may be
combined with concepts from other domains through semantic reasoning.

---

# Design Principles

## Renderer Independent

Composition concepts never describe renderer syntax, software
parameters, or layout APIs.

Examples of excluded information include:

- renderer-specific composition syntax
- bounding box formats
- scene graph implementations
- viewport controls
- crop parameters
- render resolution

These belong exclusively to Renderer Adapters.

---

## Creative Representation

Composition represents visual organization rather than implementation.

For example:

- Rule of Thirds
- Symmetry
- Negative Space
- Leading Lines

rather than:

- crop image
- move camera
- define bounding boxes
- generate layout JSON

Renderer Adapters determine how Composition is translated into the
capabilities of each rendering system.

---

## Spatial Representation

Composition represents **spatial intent** independently of technical
implementation.

Creators may describe:

- visual hierarchy
- relative positioning
- subject dominance
- spatial relationships
- framing
- regions of interest
- layout constraints
- negative space
- reading flow
- visual priority

Renderer Adapters determine how these intentions are represented.

For example, different renderers may express spatial intent through:

- layout constraints
- scene graphs
- semantic regions
- object placement systems
- bounding regions
- future spatial composition APIs

The Creative Representation remains unchanged.

---

## Reusable Knowledge

Composition concepts are reusable across:

- photography
- cinema
- illustration
- concept art
- animation
- game cinematics
- graphic design
- product visualization
- future rendering technologies

---

## Semantic Relationships

Composition concepts participate in semantic relationships throughout
the Creative Knowledge Ecology.

For example:

Negative Space

may be associated with:

- Minimalism
- Isolation
- Elegance
- Simplicity
- Luxury

Likewise,

Leading Lines

may be associated with:

- Journey
- Motion
- Perspective
- Focus
- Depth

These relationships enable probabilistic reasoning within the Visual
Meaning Layer (VML).

---

# Creative Concepts

Examples include:

## Balance

- Symmetry
- Asymmetry
- Radial Balance
- Dynamic Balance

## Framing

- Centered Composition
- Rule of Thirds
- Golden Ratio
- Frame Within Frame

## Direction

- Leading Lines
- Visual Flow
- Eye Path
- Directional Emphasis

## Space

- Negative Space
- Positive Space
- Layered Depth
- Foreground Emphasis
- Background Separation

## Perspective

- Forced Perspective
- Scale Contrast
- Depth Compression
- Expansive Space

## Narrative Composition

- Subject Isolation
- Environmental Storytelling
- Juxtaposition
- Visual Contrast
- Repetition
- Visual Rhythm

The Composition domain is intentionally extensible.

New Creative Concepts may be introduced without modifying the overall
architecture.

---

# Spatial Intent

In addition to Creative Concepts, Composition may describe spatial
intent.

Spatial intent represents **where creative elements belong within a
Creative Representation**, without prescribing how renderers implement
those decisions.

Examples include:

- Primary subject location
- Secondary subject location
- Relative scale
- Subject dominance
- Layer ordering
- Regions of interest
- Reserved negative space
- Typography safe areas
- Reading direction
- Visual priority

These descriptions remain renderer-independent.

Renderer Adapters translate them into the capabilities of individual
rendering systems.

---

# Relationship with Camera

Camera determines **how the scene is observed**.

Composition determines **how visual information is organized**.

Camera answers:

> **Where is the audience observing from?**

Composition answers:

> **How is visual meaning organized?**

A change in Camera may preserve Composition.

Likewise, a new Composition may be achieved using different Camera
configurations.

These domains complement one another while remaining independent.

---

# Relationship with Dynamics

Dynamics describes the perceived energy of a Creative Representation.

Composition describes how that energy is visually organized.

For example:

Diagonal composition

may reinforce:

- motion
- instability
- urgency

Symmetrical composition

may reinforce:

- calm
- order
- authority
- permanence

Composition amplifies the perception of Dynamics.

---

# Relationship with Narrative

Narrative defines **why** a moment exists.

Composition determines **how that moment is visually communicated**.

The same Narrative may be expressed through multiple compositional
approaches.

Likewise, the same Composition may support different Narrative
interpretations.

Meaning emerges from their interaction.

---

# Role within VizClick

Composition concepts are selected by creators to organize visual meaning.

The Visual Meaning Layer (VML) may activate related Composition concepts
through semantic reasoning.

Creators remain free to:

- accept recommendations
- ignore recommendations
- extend them through Custom Creative Intent (CCI)

The final Composition Brief combines:

- Activated Creative Concepts
- Recommended Concepts
- Spatial Intent
- Custom Creative Intent (CCI)

Together they represent both semantic understanding and human creative
direction.

---

# Guiding Principle

> Composition represents the visual language of organization.
>
> It defines how meaning is arranged within a Creative Representation,
> while Renderer Adapters determine how that organization is realized by
> individual rendering technologies.