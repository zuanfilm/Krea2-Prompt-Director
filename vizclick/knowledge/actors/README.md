# Actors

> **The creative domain that represents the entities participating in a Creative Representation.**

Actors are one of the core domains of the **Creative Knowledge Ecology (CKE)**.

An Actor represents any entity that can exist within a scene and
participate in visual storytelling.

Actors are renderer-independent.

They describe **creative identity and narrative function** rather than
visual implementation.

---

# Purpose

The Actors domain provides reusable Creative Concepts that describe the
subjects of a creative scene.

Actors define:

- Identity
- Role
- Presence
- Relationships
- Behavior
- Narrative importance
- Visual focus
- Interaction with the environment
- Interaction with other Actors

Actors form the foundation upon which creative scenes are constructed.

---

# Design Principles

## Renderer Independent

Actors never describe renderer syntax, software parameters, or
implementation details.

Examples of excluded information include:

- prompt syntax
- model-specific tokens
- renderer keywords
- software parameters

These belong exclusively to Renderer Adapters.

---

## Creative Representation

Actors represent creative identity rather than rendered appearance.

For example:

- Explorer
- Samurai
- Cat
- Dragon
- Oak Tree

rather than implementation details such as:

- ultra detailed
- photorealistic
- octane render
- 8k

---

## Reusable Knowledge

Actor concepts are reusable across:

- photography
- cinema
- animation
- illustration
- concept art
- game cinematics
- virtual production
- future rendering technologies

---

## Semantic Relationships

Actors participate in semantic relationships throughout the Creative
Knowledge Ecology.

For example:

Knight

may be associated with:

- Armor
- Sword
- Honor
- Medieval Architecture
- Horse
- Castle

These relationships enable probabilistic reasoning within the Visual
Meaning Layer (VML).

---

# Actor Categories

The Actors domain is intentionally broad.

Examples include:

## Humans

- Adult
- Child
- Elder
- Explorer
- Scientist
- Athlete
- Musician

## Animals

- Cat
- Dog
- Eagle
- Horse
- Wolf
- Bear

## Fantasy

- Dragon
- Elf
- Orc
- Fairy
- Giant
- Phoenix

## Science Fiction

- Android
- Alien
- Robot
- Cyborg
- Space Marine

## Nature

- Tree
- Flower
- Mushroom
- Coral
- Mountain
- River

## Objects

- Vehicle
- Building
- Ship
- Spaceship
- Statue
- Book

The Actors domain is intentionally extensible.

New Actor concepts may be introduced without modifying the overall
architecture.

---

# Actor Composition

Actors are represented through reusable Creative Concepts.

During creative reasoning, the Visual Meaning Layer (VML) may activate
additional concepts related to an Actor.

For example:

Explorer

may activate:

- Backpack
- Compass
- Adventure
- Wilderness
- Curiosity

Creators remain free to:

- accept recommendations
- ignore recommendations
- extend them through Custom Creative Intent (CCI)

The resulting Actor Brief combines semantic understanding with human
creative direction.

---

# Relationships

Actors rarely exist in isolation.

They interact with:

- other Actors
- Environments
- Lighting
- Camera
- Motion
- Materials
- Narrative

These interactions are represented through explicit Relationships within
the Creative Knowledge Ecology.

---

# Role within VizClick

Actors provide the primary entities around which Creative Briefs are
constructed.

The Visual Meaning Layer (VML) reasons about Actors using semantic
relationships.

The Activation Network discovers related concepts.

Custom Creative Intent (CCI) allows creators to introduce entirely new
or intentionally unconventional Actors without modifying the Creative
Knowledge Ecology.

---

# Guiding Principle

> Actors represent the participants of a creative scene.
>
> They describe creative identity rather than rendered appearance.