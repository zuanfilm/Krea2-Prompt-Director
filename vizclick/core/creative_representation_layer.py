"""
VizClick - Creative Representation Layer (CRL)

The Creative Representation Layer (CRL) is the canonical,
renderer-independent representation of creative intent.

It organizes creative decisions into structured Creative Briefs
before they are compiled and translated by Renderer Adapters.

The CRL is the core domain model of VizClick.

It is NOT:
- a prompt
- a renderer
- an AI model

It IS:
- a structured representation of creative intent
- the source of truth for every creative project
- independent from Krea, Flux, Qwen, or any future renderer
"""

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class CreativeRepresentationLayer:
    """
    Central representation of a creative project.

    The Creative Representation Layer (CRL) stores all creative
    decisions in a renderer-independent format.

    Each category represents a Creative Brief.

    The CRL is later compiled into a Production Brief and translated
    through Renderer Adapters.
    """

    creative_brief: str = ""

    subjects: Dict[str, Any] = field(default_factory=dict)

    style: Dict[str, Any] = field(default_factory=dict)

    lighting: Dict[str, Any] = field(default_factory=dict)

    camera: Dict[str, Any] = field(default_factory=dict)

    emotion: Dict[str, Any] = field(default_factory=dict)

    pose: Dict[str, Any] = field(default_factory=dict)

    composition: Dict[str, Any] = field(default_factory=dict)

    location: Dict[str, Any] = field(default_factory=dict)

    color_palette: Dict[str, Any] = field(default_factory=dict)

    director_notes: Dict[str, Any] = field(default_factory=dict)

    story: Dict[str, Any] = field(default_factory=dict)

    def summary(self) -> dict:
        """
        Returns a readable representation of the current
        Creative Representation Layer.

        This method is primarily intended for debugging
        and inspection during development.
        """

        return {
            "creative_brief": self.creative_brief,
            "subjects": self.subjects,
            "style": self.style,
            "lighting": self.lighting,
            "camera": self.camera,
            "emotion": self.emotion,
            "pose": self.pose,
            "composition": self.composition,
            "location": self.location,
            "color_palette": self.color_palette,
            "director_notes": self.director_notes,
            "story": self.story,
        }