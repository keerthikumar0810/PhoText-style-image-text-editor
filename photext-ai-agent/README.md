# Photext AI Agent

Photext AI Agent is an intelligent system that orchestrates multiple AI agents to perform advanced image processing, text detection, font analysis, and intelligent image editing tasks. The frontend integrates with a set of backend agents that handle localized OCR, semantic background recovery, and seamless text re-rendering.

## Architecture Interaction Graph

```text
                +----------------+
                |   User Input   |
                +-------+--------+
                        |
                        v
             +----------------------+
             | Orchestrator Agent   |
             +----+-----+-----+-----+
                  |     |     |
                  |     |     |
          +-------+     |     +--------+
          |             |              |
          v             v              v
   OCR Agent      Font Agent     Image Agent
          |             |              |
          +-------------+--------------+
                        |
                        v
               Editing Agent
                        |
                        v
               Export Agent
                        |
                        v
                  Final Output
```

## Core Agent Workflow

```text
                    User Uploads Image
                            │
                            ▼
                  ┌──────────────────┐
                  │ OrchestratorAgent│
                  └────────┬─────────┘
                           │
          ┌────────────────┼─────────────────┐
          ▼                ▼                 ▼
   OCRAgent          FontAgent        ImageEditorAgent
      │                  │                   │
      ▼                  ▼                   ▼
 Detect Text      Detect Fonts       Create Canvas
 Bounding Boxes      Colors           Overlay Layers
      │                  │                   │
      └──────────────┬───┴───────────────────┘
                     ▼
              Editing Workflow
                     │
         User Selects Text Region
                     │
                     ▼
           Replace / Move / Resize
                     │
                     ▼
             Apply Font Styling
                     │
                     ▼
              Background Recovery
                     │
                     ▼
              Live Canvas Update
                     │
                     ▼
               ExportAgent
                     │
          JPG / PNG / PDF Output
                     │
                     ▼
                Download Image
```

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`

## Overall System Architecture

```text
                     Browser UI
                          │
                          ▼
                ADK Root Orchestrator
                          │
     ┌───────────────┬───────────────┬───────────────┐
     ▼               ▼               ▼               ▼
 OCR Agent     Font Agent     Edit Agent     Export Agent
     │               │               │               │
     └───────────────┴───────┬───────┴───────────────┘
                             ▼
                     Shared Session State
                             │
                             ▼
                    Image Processing Tools
                             │
                             ▼
                     Final Download Output 
```
