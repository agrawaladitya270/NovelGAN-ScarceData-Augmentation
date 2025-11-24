# 🎨 Anime GAN Project

**Generative Adversarial Networks (GANs) for Anime Face Synthesis**

This project explores multiple GAN architectures — **DCGAN**, **SAGAN** — trained on anime face datasets. Each model is implemented and trained in standalone Jupyter notebooks (Colab-ready), using Google Drive for data access instead of storing datasets in the repository.

---

## 🧩 Project Overview

| Model | Architecture | Key Idea | Notebook |
|:------|:-------------|:----------|:-----------|
| **DCGAN** | Deep Convolutional GAN | Baseline convolutional generator–discriminator pair | `01_dcgan_anime.ipynb` |
| **SAGAN** | Self-Attention GAN | Adds attention layers for long-range feature modeling | `02_sagan_anime.ipynb` |

---

## 🧠 Goals

- Learn and compare how convolutional, attention-based, and hybrid GANs generate anime faces.  
- Analyze qualitative differences (sharpness, diversity, stability).  
- Develop a clean, reproducible workflow entirely on **Google Colab** with **Drive-based datasets**.  

---

## 📁 Repository Structure

```

anime-gan-project/
├── notebooks/
│   ├── 01_dcgan_anime.ipynb
│   └── 02_sagan_anime.ipynb
├── results/       
├── README.md
├── requirements.txt
└── .gitignore

````
## 👤 Author

**Aditya Agrawal**
Machine Learning Engineer • IIT Delhi Graduate
