# VizClick Architecture

## 1. Overview

## 2. System Philosophy

## 3. High-Level Architecture

## 4. Core Systems

### VCSG — VizClick Scene Graph

### VCKB — VizClick Knowledge Base

### VCAR — VizClick Asset Registry

### VCIF — VizClick Intelligence Framework

### VCSC — VizClick Scene Compiler

### VCEP — VizClick Export Profiles

### VCLF — VizClick Localization Framework

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

          VizClick Scene Graph (KSG)

                      │

      ┌───────────────┼───────────────┐

      ▼               ▼               ▼

 Knowledge       Assets          Inspector
 Base (KKB)      (KAR)           

                      │

                      ▼

          VizClick Scene Compiler

                      │

                      ▼

          Export Profile (KEP)

                      │

                      ▼

              AI Model Prompt

The Scene Graph is the central representation of creative intent. Prompts are generated outputs, not the source of truth.

Separation of Responsibilities

System	Responsibility
UI	User interaction
VCSG	Creative structure
VCKB	Visual knowledge
VCAR	Reusable assets
VCIF	AI assistance
VCSC	Prompt generation
VCEP	Model optimization
VCLF	Language presentation

| System | Responsibility        |
| ------ | --------------------- |
| UI     | User interaction      |
| VCSG    | Creative structure    |
| VCKB    | Visual knowledge      |
| VCAR    | Reusable assets       |
| VCIF    | AI assistance         |
| VCSC    | Prompt generation     |
| VCEP    | Model optimization    |
| VCLF    | Language presentation |

ComfyUI Integration Philosophy

VizClick2 should not fight ComfyUI.

It should complement it.

The relationship:

ComfyUI

      +
      
VizClick

      ↓

Creative Intelligence Layer

ComfyUI handles:

workflow execution
models
samplers
images
nodes

VizClick2 handles:

creative planning
scene organization
prompt intelligence
localization
visual direction


Future compatibility

Today:

VizClick2 → Flux3

Tomorrow:

VizClick2 → Flux3
VizClick2 → Qwen Image
VizClick2 → Ideogram
VizClick2 → Video Models
VizClick2 → 3D Tools




