# Architecture

## Architectural Principle

VizClick models creativity.

It does not model rendering technology.

Every renderer, language model, vision model, or visualization engine is treated as an interchangeable backend.

The architecture is intentionally centered around semantic reasoning instead of AI capabilities.

```
Imagination
        │
        ▼
Creative Representation Layer
        │
        ▼
Visualization
```

The Creative Representation Layer consists of four primary components:

- Creative Ontology
- Activation Network
- Production Brief
- VML

Together these components represent creative intent independently from any renderer.

Renderer adapters simply compile this representation into technologies such as Krea, FLUX, ComfyUI, Veo, Blender, Unreal Engine, or future visualization systems.

This separation guarantees that VizClick evolves independently from AI model lifecycles.