🏗️ Define Krea2 System Architecture
# Krea2 Prompt Director Architecture

## 1. Overview

## 2. System Philosophy

## 3. High-Level Architecture

## 4. Core Systems

### KSG — Krea Scene Graph

### KKB — Krea Knowledge Base

### KAR — Krea Asset Registry

### KIF — Krea Intelligence Framework

### KSC — Krea Scene Compiler

### KEP — Krea Export Profiles

### KLF — Krea Localization Framework

## 5. User Interface Architecture

## 6. ComfyUI Integration

## 7. Data Flow

## 8. Extension System

## 9. Future Compatibility
                    USER

                      │

                      ▼

              Interface Layer

                      │

                      ▼

          Krea Scene Graph (KSG)

                      │

      ┌───────────────┼───────────────┐

      ▼               ▼               ▼

 Knowledge       Assets          Inspector
 Base (KKB)      (KAR)           

                      │

                      ▼

          Krea Scene Compiler

                      │

                      ▼

          Export Profile (KEP)

                      │

                      ▼

              AI Model Prompt

The Scene Graph is the central representation of creative intent. Prompts are generated outputs, not the source of truth.

Separation of Responsibilities

Example:

System	Responsibility
UI	User interaction
KSG	Creative structure
KKB	Visual knowledge
KAR	Reusable assets
KIF	AI assistance
KSC	Prompt generation
KEP	Model optimization
KLF	Language presentation

| System | Responsibility        |
| ------ | --------------------- |
| UI     | User interaction      |
| KSG    | Creative structure    |
| KKB    | Visual knowledge      |
| KAR    | Reusable assets       |
| KIF    | AI assistance         |
| KSC    | Prompt generation     |
| KEP    | Model optimization    |
| KLF    | Language presentation |

ComfyUI Integration Philosophy

Very important.

Krea2 should not fight ComfyUI.

It should complement it.

The relationship:

ComfyUI

      +
      
Krea2 Prompt Director

      ↓

Creative Intelligence Layer

ComfyUI handles:

workflow execution
models
samplers
images
nodes

Krea2 handles:

creative planning
scene organization
prompt intelligence
localization
visual direction


Future compatibility

Today:

Krea2 → Krea

Tomorrow:

Krea2 → Flux
Krea2 → Qwen Image
Krea2 → SDXL
Krea2 → Video Models
Krea2 → 3D Tools




