# 🎼 **`app/` — Core Application Package**

This folder contains the foundational modules for the **LLMOps Music Composer**.
All music-generation logic, audio utilities, and future LLM-based composition components will live inside this package.

At the current stage, the package includes utilities for generating audio from notes and an LLM interface for melody, harmony, rhythm, and style generation. Later branches will expand this into a full composition pipeline with embeddings and structured generation workflows.

## 📁 **Folder Overview**

```text
app/
├── __init__.py        # Marks this directory as a Python package
├── utils.py           # Music/audio helper functions (freq conversion + WAV synthesis)
└── main.py            # NEW: LLM-based melody, harmony, rhythm, and style generation
```

## 🎧 **Current Modules**

### `utils.py`

Provides core audio-utility functions used throughout the project:

* Convert note names (e.g., “C4”, “G3”, “A#4”) into frequencies using `music21`
* Generate WAV audio clips via sine-wave synthesis
* Return WAV bytes suitable for:

  * saving to disk
  * API responses
  * embedding in UI layers (Flask/Streamlit)

This module forms the foundation for audio playback and melody evaluation.

### `main.py`

Implements the first LLM-driven musical-generation engine:

* Generates melodies as note sequences
* Produces harmony chord progressions
* Suggests rhythm durations
* Adapts melody+harmony+rhythm into stylistic variations (jazz, baroque, lofi, etc.)

This class (`MusicLLM`) acts as the core interface between your Groq-hosted LLaMA model and all musical reasoning tasks in the project.

## 🚀 **What This Folder Will Contain Later**

Future branches will expand the `app/` package with:

* A composition pipeline combining melody, harmony, rhythm, and style
* Embedding and retrieval modules for musical pattern matching
* Audio transformations, mixing, and arrangement utilities
* Integration layers for UI, API endpoints, or interactive composition interfaces

The structure remains intentionally lightweight, ensuring clean growth as more LLMOps components are introduced.