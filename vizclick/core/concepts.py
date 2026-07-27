"""
VizClick Creative Concept

Defines the fundamental ontology object used throughout VizClick.

Every YAML concept is loaded into a CreativeConcept instance.
The object intentionally supports more fields than V0 currently
requires so that future versions (VCCE, semantic reasoning,
recommendations, etc.) can reuse the same data model.

Author: VizClick
License: Apache-2.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CreativeConcept:
    """
    Represents a single concept in the VizClick Knowledge Ecology.

    Examples
    --------
    lighting.soft_diffused
    camera.low_angle
    composition.rule_of_thirds
    performance.confident
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    id: str
    name: str
    category: str

    # ------------------------------------------------------------------
    # Knowledge Layer
    # ------------------------------------------------------------------

    essence: str = ""

    # ------------------------------------------------------------------
    # Creative Layer
    # ------------------------------------------------------------------

    creative_intent: str = ""

    # ------------------------------------------------------------------
    # Renderer Layer
    # ------------------------------------------------------------------

    production_description: str = ""

    # ------------------------------------------------------------------
    # Visual Knowledge
    # ------------------------------------------------------------------

    visual_characteristics: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Semantic Layer
    # ------------------------------------------------------------------

    relationships: dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Educational Layer
    # ------------------------------------------------------------------

    common_applications: list[str] = field(default_factory=list)

    expert_notes: str = ""

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------

    @property
    def full_name(self) -> str:
        """
        Human-readable identifier.

        Example:
            Lighting • Soft Diffused Lighting
        """
        return f"{self.category} • {self.name}"

    def __str__(self) -> str:
        return self.full_name

    def __repr__(self) -> str:
        return (
            f"CreativeConcept("
            f"id='{self.id}', "
            f"category='{self.category}', "
            f"name='{self.name}')"
        )