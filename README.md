# 🎼 **Utilities Functions for Audio Generator — LLMOps Music Composer**

This branch adds the first functional component to the project: the audio-generation utilities.
These functions allow musical note names to be converted into frequencies and then synthesised into WAV audio, forming the foundation for all future music-generation features.

## 🗂️ **Updated Project Structure**

Only the **new file** is annotated.

```text
LLMOPS-MUSIC-COMPOSER/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.py
├── llmops_music_composer.egg-info/
│
└── app/
    ├── __init__.py
    └── utils.py        # NEW: Utility functions for note→frequency and WAV synthesis
```

## 🎧 **What This Branch Introduces**

### 🎵 Note-to-Frequency Conversion

Uses `music21` to transform readable note labels (e.g., "C4", "A#3") into accurate pitch frequencies in Hz.

### 🔊 WAV Synthesis from Frequencies

Uses a sine-wave synthesiser to generate short audio clips from those frequencies, returned as raw WAV bytes suitable for saving, streaming, or embedding in an API/UI.

These utilities form the first core building block of the LLMOps Music Composer and will support higher-level composition logic in later branches.