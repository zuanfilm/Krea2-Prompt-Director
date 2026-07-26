"""
VizClick - Creative Concept

A Creative Concept is the smallest reusable unit of creative knowledge
within the Creative Knowledge Ecology (CKE).

Creative Concepts are renderer-independent and represent knowledge
about creative ideas, not prompts or implementation details.

Examples:
    - Soft Diffused Lighting
    - Editorial Fashion
    - Golden Hour
    - Rule of Thirds
    - Luxury
    - Rain
    - Marble

A Creative Concept describes:

    • What the concept is
    • Why creators use it
    • How it relates to other creative concepts

Creative Concepts are the foundation of VizClick's
Creative Representation Layer (CRL).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class CreativeRelationships:
    """
    Semantic relationships between Creative Concepts.

    These relationships are renderer-independent and describe how
    concepts naturally interact within creative practice.
    """

    supports: Dict[str, float] = field(default_factory=dict)

    combines_with: Dict[str, float] = field(default_factory=dict)

    avoids: Dict[str, float] = field(default_factory=dict)

    influences: Dict[str, float] = field(default_factory=dict)

    commonly_used_in: List[str] = field(default_factory=list)


@dataclass(slots=True)
class CreativeMetadata:
    """
    Maintenance information for a Creative Concept.

    Metadata never affects creative reasoning.
    It exists only to help manage and evolve the knowledge base.
    """

    version: str = "1.0"

    author: str = ""

    confidence: float = 1.0

    sources: List[str] = field(default_factory=list)

    last_updated: str = ""


@dataclass(slots=True)
class CreativeConcept:
    """
    The smallest reusable unit of creative knowledge.

    Creative Concepts are immutable pieces of domain knowledge that
    can be combined into Creative Briefs and ultimately compiled into
    a Production Brief.

    They never contain renderer-specific information.
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    id: str

    name: str

    category: str

    # ------------------------------------------------------------------
    # Meaning
    # ------------------------------------------------------------------

    essence: str

    guiding_question: str

    # ------------------------------------------------------------------
    # Creative Knowledge
    # ------------------------------------------------------------------

    creative_relationships: CreativeRelationships = field(
        default_factory=CreativeRelationships
    )

    # ------------------------------------------------------------------
    # Maintenance
    # ------------------------------------------------------------------

    metadata: CreativeMetadata = field(default_factory=CreativeMetadata)

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    @property
    def is_renderer_independent(self) -> bool:
        """Creative Concepts are always renderer independent."""
        return True

    def summary(self) -> dict:
        """
        Returns a simplified representation useful for debugging,
        inspection, and future tooling.
        """

        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "essence": self.essence,
            "guiding_question": self.guiding_question,
            "creative_relationships": {
                "supports": self.creative_relationships.supports,
                "combines_with": self.creative_relationships.combines_with,
                "avoids": self.creative_relationships.avoids,
                "influences": self.creative_relationships.influences,
                "commonly_used_in": self.creative_relationships.commonly_used_in,
            },
            "metadata": {
                "version": self.metadata.version,
                "author": self.metadata.author,
                "confidence": self.metadata.confidence,
                "sources": self.metadata.sources,
                "last_updated": self.metadata.last_updated,
            },
        }