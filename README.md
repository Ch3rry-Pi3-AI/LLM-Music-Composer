# 🎼 **LLMOps Music Composer — Project Overview**

This repository presents a complete **LLMOps workflow** for an AI-powered **Music Composer**, combining Groq-hosted LLMs, Streamlit UI, WAV synthesis, Kubernetes deployment, and a full GitLab CI/CD pipeline.

The system transforms natural-language prompts into melody, harmony, rhythm, and style-adapted compositions. These are synthesised into audio and deployed automatically to GKE via GitLab.

<p align="center">
  <img src="img/streamlit/streamlit_app.gif" alt="AI Music Composer Demo" width="100%">
</p>

## 🧩 **Grouped Stages**

|     #     | Stage                                   | Description                                                                                                                                                                                            |
| :-------: | :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   **00**  | **Project Setup**                       | Created the base folder layout, virtual environment, editable install, `.env` handling, and foundational configuration for clean modular development.                                                  |
| **01–02** | **Core Logic (Utilities + LLM Module)** | Implemented audio utilities (`utils.py`) for note→frequency conversion and WAV synthesis, plus the `MusicLLM` module powering melody, harmony, rhythm, and style generation using Groq’s LLaMA models. |
|   **03**  | **Streamlit Application**               | Built a user-friendly Streamlit UI (`application.py`) to accept prompts, choose styles, generate music, and play back synthesised audio. Included improved UX, layout, spinners, and session logic.    |
|   **04**  | **Docker & Kubernetes Deployment**      | Added the project `Dockerfile` and `kubernetes-deployment.yaml` to deploy the Streamlit app onto GKE with secure secret injection via Kubernetes secrets.                                              |
|   **05**  | **GitLab Project Setup**                | Created a GitLab remote for CI/CD, added GitLab authentication, and configured project access for pipeline usage.                                                                                      |
|   **06**  | **Google Cloud Platform Setup**         | Enabled required GCP APIs, created the GKE cluster, created Artifact Registry, set up service accounts, and configured secure deployment access.                                                       |
|   **07**  | **GitLab CI/CD Pipeline**               | Implemented `.gitlab-ci.yml` for automated Docker builds, Artifact Registry pushes, and GKE deployments. Added GCP credentials, Kubernetes secrets, and full GitLab pipeline flow.                     |

## 🗂️ **Project Structure**

```text
LLMOPS-MUSIC-COMPOSER/
├── app/                                    # 🎵 Core application logic
│   ├── __pycache__/                        # ⚡ Python cache
│   ├── __init__.py                         # Marks the app package
│   ├── main.py                             # 🤖 LLM module for melody/harmony/rhythm/style generation
│   ├── README.md                           # 📖 Documentation for the app folder
│   └── utils.py                            # 🔊 Note→frequency + WAV synthesis utilities
│
├── img/                                    # 📸 Documentation screenshots & GIFs
│   └── streamlit/
│       └── streamlit_app.gif               # 🎬 Demo of the Streamlit music generator
│
├── llmops_music_composer.egg-info/         # 📦 Packaging metadata (auto-generated)
├── .venv/                                  # 🧪 Virtual environment (ignored in repo)
├── .env                                    # 🔐 API keys (never committed)
├── .gitignore                              # 🚫 Ignore rules
├── .gitlab-ci.yml                          # ⚙️ GitLab CI/CD pipeline for build + deploy
├── .python-version                         # 🐍 Python version pin
├── application.py                          # 🎛️ Streamlit application UI
├── Dockerfile                              # 🐳 Container build definition
├── gcp-key.json                            # 🔑 GCP service account key (ignored from repo)
├── kubernetes-deployment.yaml              # ☸️ GKE deployment + service manifest
├── pyproject.toml                          # 🧩 Project metadata + dependencies
├── README.md                               # 📘 Main project documentation (you are here)
├── requirements.txt                        # 📦 Python dependencies list
├── setup.py                                # 🔧 Editable install configuration
└── uv.lock                                 # 🔒 Locked dependency versions
```

## 🚀 **Summary**

The **LLMOps Music Composer** project demonstrates how to take a creative, LLM-powered idea from prototype to a fully automated, cloud-deployed system.

The full workflow includes:

* A **Groq-based LLM engine** generating melodies, harmonies, rhythms, and style-adapted musical structures
* A **Streamlit UI** for composing and playing music interactively
* A solid MLOps backbone with:

  * **Docker containerisation**
  * **Kubernetes deployment (GKE)**
  * **Artifact Registry**
  * **Google Cloud service accounts & secrets**
  * **GitLab CI/CD pipeline** for automated build & deploy
* Proper project structuring, modularisation, and dev-tooling

Together, these stages form a complete **LLMOps pipeline**, turning text prompts into fully generated music — deployed, scaled, and automated in the cloud.
