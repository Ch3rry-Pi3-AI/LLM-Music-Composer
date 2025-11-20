# ☁️ **GCP Environment Setup — LLMOps Music Composer**

This branch introduces the full **Google Cloud Platform setup** required for deploying and operating the LLMOps Music Composer.
It covers API activation, GKE cluster creation, Artifact Registry configuration, and preparing a Service Account that will later enable CI/CD pipelines to deploy containers automatically.

This stage establishes the cloud infrastructure backbone for upcoming GitLab CI/CD and Kubernetes deployment branches.

<p align="center">
  <img src="IMG/gcp_setup/networking.png" alt="GCP Networking Configuration" width="100%">
</p>

## 🗂️ **Updated Project Structure**

Only the **new setup stage** is represented; no new code files were added for this branch.

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
├── IMG/                         # Contains GCP setup screenshots (networking, etc.)
├── app/
│   ├── __init__.py
│   ├── utils.py
│   └── main.py
├── application.py
├── Dockerfile
└── kubernetes-deployment.yaml
```

## 🌐 **What This Branch Introduces**

### ✅ **Enable Required GCP APIs**

In your GCP Console:

Navigation:
**APIs & Services → Library**

Enable these essential services:

* Kubernetes Engine API
* Container Registry API
* Compute Engine API
* Cloud Build API
* Cloud Storage API
* IAM API

These APIs allow Kubernetes clusters, container storage, compute resources, and identity/permission systems to function correctly.



## ☸️ **Create GKE Cluster and Artifact Registry**

### **1. Create a GKE Cluster**

1. In the GCP Console, search for **GKE** → open *Kubernetes Engine*.
2. Create a new cluster (Autopilot or Standard — your choice).
3. Under **Networking**, apply the necessary configuration.

<p align="center">
  <img src="IMG/gcp_setup/networking.png" alt="GKE Networking Setup" width="100%">
</p>

### **2. Create an Artifact Registry Repository**

1. Search for **Artifact Registry**.
2. Create a new repository.
3. Choose **Format: Docker**.
4. Select the **same region** as your cluster.

This store will hold all container images built from your Dockerfile.



## 🔐 **Create a Service Account and Configure Access**

### **1. Create a Service Account**

In the GCP Console → **IAM & Admin → Service Accounts**.
Create a new one for CI/CD usage.

### **2. Assign These Roles:**

* Storage Object Admin
* Storage Object Viewer
* Owner
* Artifact Registry Admin
* Artifact Registry Writer

These permissions allow the CI/CD pipeline to push container images and deploy to Kubernetes.

### **3. Download the Key File (.json)**

1. Click **Actions** on your service account
2. **Manage keys**
3. **Add key → Create new key**
4. Download the JSON file (e.g., `gcp-key.json`)

### **4. Place the Key in Your Project Root**

Move it into your project:

```
LLMOPS-MUSIC-COMPOSER/gcp-key.json
```

### **5. Add to .gitignore**

To prevent credential leaks:

```
gcp-key.json
```
