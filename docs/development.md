# VizClick Development Guidelines

## 1. Development Philosophy

## 2. Technology Stack

## 3. Repository Structure

## 4. Python Standards

## 5. Naming Conventions

## 6. Code Organization

## 7. Data Architecture

## 8. Adding New Features

## 9. Adding Knowledge Base Content

## 10. Adding AI Providers

## 11. Adding Localization

## 12. ComfyUI Node Development

## 13. Testing Strategy

## 14. Git Workflow

## 15. Contribution Guidelines

---------------------------------------

## 1. Development Philosophy

VizClick is built around the principle:

"Build for the artist. Abstract the technology."

Code decisions should prioritize:

- Creative clarity
- Maintainability
- Extensibility
- User experience
- Model independence

Technical complexity should remain behind the creative interface whenever possible.

---------------------------------------

## Technology Stack

Primary Language:
Python 3.11+

Framework:
ComfyUI Custom Nodes

Interface:
ComfyUI Node System

Data Format:
JSON / YAML

Documentation:
Markdown

Version Control:
Git + GitHub

---------------------------------------------
## Python Standards

VizClick follows:

- PEP 8 style guidelines
- Type hints whenever possible
- Clear class responsibilities
- Small focused modules
- Documentation strings for public classes
- ---------------------------------------------

Classes:

PascalCase

SceneGraph
ExportProfile
CreativeAdvisor


Functions:

snake_case

compile_scene()
load_profile()
analyze_subject()


Constants:

UPPER_CASE

DEFAULT_LANGUAGE
SUPPORTED_MODELS
-----------------------------------------
## Code Organization

Each folder represents a responsibility.

core/
    Fundamental systems

knowledge/
    Creative vocabulary

nodes/
    ComfyUI integration

exporters/
    Model-specific translation

localization/
    Interface languages

providers/
    AI intelligence connectors
-----------------------------------------

AI PROVIDER

A provider must never modify the Scene Graph.

Flow:

Scene Graph

↓

Provider Adapter

↓

Creative Analysis

↓

Suggestions
-----------------------------------------
Adding new languages
Interface language ≠ Prompt language.

Example:

A Japanese artist can use:

Interface:
日本語

Export:
English

or:

Interface:
English

Export:
Japanese

-----------------------------------------

🎬 Feature: Add Scene Graph foundation

🐛 Fix: Correct localization loading

📚 Docs: Update architecture

🎨 Asset: Add cinematic lighting presets

⚙️ Refactor: Improve exporter structure
-----------------------------------------
## VizClick Development Motto

Every technical decision should answer:

"Does this help artists express their vision?"

If yes, continue.

If no, reconsider.

depending on the model.
