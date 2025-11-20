# 🏗️ **Initial Project Setup — LLMOps Music Composer**

This branch establishes the foundational structure for the **LLMOps Music Composer** project.
It introduces the base Python package layout, editable installation setup, environment configuration, and the core scaffolding needed for future branches involving embeddings, melody generation, and LLM-assisted composition workflows.

The setup is intentionally lightweight, ready to be expanded cleanly in later stages.

## 🗂️ **Project Structure**

```text
LLMOPS-MUSIC-COMPOSER/
├── .venv/                                # Virtual environment
├── .env                                  # Environment variables (API keys for future models)
├── .gitignore                            # Standard ignores: venv, __pycache__, .env, build artefacts
├── .python-version                       # Python version pin
├── pyproject.toml                        # Project metadata and dependency configuration
├── README.md                             # Root documentation
├── requirements.txt                      # Python dependencies (exported)
├── setup.py                              # Editable install configuration
│
├── llmops_music_composer.egg-info/       # Auto-generated metadata from editable install
│
└── app/                                  # Core application package
    └── __init__.py                       # Marks app as a package
```

> 💡 The `.env` file will eventually hold keys for Groq, HuggingFace, or audio-generation APIs — and must never be committed.

## ⚙️ **What Was Done in This Branch**

### 1. **Base project layout created**

* Added `app/` with an `__init__.py` so the package imports cleanly.
* Ensured the folder structure is ready for future modules (LLM logic, composition engine, embeddings, etc.).

### 2. **Environment + dependency setup**

* Created `.venv/` for isolated development.
* Added `.python-version` for consistency across environments.
* Added `requirements.txt` and `pyproject.toml` for dependency + metadata management.

### 3. **Editable install configured**

* `setup.py` enables:

```bash
uv pip install --editable .
```

which makes imports like:

```python
from app import some_module
```

work instantly during development.

### 4. **Project prepared for next branches**

This minimal structure is ready for:

* Audio preprocessing utilities
* LLM-based music-theory reasoning
* Embedding models for melody and rhythm retrieval
* Composition pipelines
* Future CI/CD, containerisation, and deployment flows

## ✅ **Summary**

This setup branch provides a clean, expandable foundation for the LLMOps Music Composer:

* Lightweight but scalable layout
* Editable package install ready
* Environment variable support prepared
* No unnecessary components introduced yet
* Perfect for layering LLM, audio, and composition modules in the next branches