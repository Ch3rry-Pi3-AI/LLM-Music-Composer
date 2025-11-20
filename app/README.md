# 🎼 **`app/` — Core Application Package**

This folder contains the foundational modules for the **LLMOps Music Composer**.
All music-generation logic, utilities, and future LLM-based components will live inside this package.

At this stage of the project, the focus is on establishing clean, well-documented utilities for converting musical inputs into audio output. Future branches will build on this by adding melody reasoning, composition pipelines, embeddings, and model integration.

## 📁 **Folder Overview**

```text
app/
├── __init__.py        # Marks this directory as a Python package
└── utils.py           # Music/audio helper functions (documented, frequency conversion + WAV generation)
```

## 🎧 **Current Modules**

### `utils.py`

Provides core audio-utility functions used throughout the project:

* Convert human-readable notes (e.g., “C4”, “G3”, “A#4”) into frequencies using `music21`
* Generate WAV audio from a list of frequencies using a sine-wave synthesiser
* Returns WAV bytes suitable for:

  * saving to disk
  * returning through a web API
  * embedding in a Streamlit/Flask interface

This module forms the first building block for melody generation and audio preview features.

## 🚀 **What This Folder Will Contain Later**

Future branches will extend the `app/` package to include:

* LLM-based composition logic
* Embedding and retrieval modules for musical patterns
* Melody/chord generators
* API routes or interface handlers
* Audio processing and augmentation tools

The structure is intentionally minimal now, ensuring clean scalability as the Music Composer grows.