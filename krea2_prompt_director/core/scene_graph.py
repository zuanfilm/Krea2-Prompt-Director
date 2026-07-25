"""
Krea2 Prompt Director - Scene Graph

The Scene Graph is the central representation
of creative intent.

It stores visual decisions before they are
translated into model-specific prompts.
"""


from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class SceneGraph:
    """
    Central representation of a creative scene.

    The Scene Graph is not a prompt.
    It is the structured visual idea behind the prompt.
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


    def summary(self) -> dict:
        """
        Returns a readable representation
        of the current creative scene.
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
        }
