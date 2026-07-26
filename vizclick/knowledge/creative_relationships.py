"""
VizClick - Creative Relationships

Creative Relationships describe the semantic connections between
Creative Concepts within the Creative Knowledge Ecology (CKE).

These relationships are renderer-independent and express how
creative ideas naturally interact according to artistic practice.

Examples:

    Soft Diffused Lighting
        supports
            Portrait
            Luxury
            Editorial Fashion

        combines_with
            Pastel Palette
            Window Light

        avoids
            Harsh Flash

        influences
            Elegance
            Calmness

Creative Relationships never contain renderer-specific information.
They represent creative knowledge only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class CreativeRelationships:
    """
    Semantic relationships between Creative Concepts.

    Relationship values are normalized between 0.0 and 1.0,
    representing the relative strength of the relationship.

    The values are descriptive, not prescriptive.
    They guide Context Probability but never enforce decisions.
    """

    # ------------------------------------------------------------------
    # Positive Relationships
    # ------------------------------------------------------------------

    supports: Dict[str, float] = field(default_factory=dict)
    """
    Concepts that are naturally reinforced by this concept.
    """

    combines_with: Dict[str, float] = field(default_factory=dict)
    """
    Concepts that frequently appear together.
    """

    influences: Dict[str, float] = field(default_factory=dict)
    """
    Concepts whose perception or expression is affected by this concept.
    """

    # ------------------------------------------------------------------
    # Negative Relationships
    # ------------------------------------------------------------------

    avoids: Dict[str, float] = field(default_factory=dict)
    """
    Concepts that rarely coexist with this concept.
    """

    # ------------------------------------------------------------------
    # Context
    # ------------------------------------------------------------------

    commonly_used_in: List[str] = field(default_factory=list)
    """
    Creative domains where this concept is commonly applied.

    Examples:
        - Editorial Photography
        - Luxury Advertising
        - Film Noir
        - Product Photography
        - Architecture
    """

    # ------------------------------------------------------------------
    # Convenience Methods
    # ------------------------------------------------------------------

    @property
    def is_empty(self) -> bool:
        """Returns True if no relationships have been defined."""

        return (
            not self.supports
            and not self.combines_with
            and not self.influences
            and not self.avoids
            and not self.commonly_used_in
        )

    def summary(self) -> dict:
        """
        Returns a simplified representation useful for debugging
        and inspection.
        """

        return {
            "supports": self.supports,
            "combines_with": self.combines_with,
            "influences": self.influences,
            "avoids": self.avoids,
            "commonly_used_in": self.commonly_used_in,
        }