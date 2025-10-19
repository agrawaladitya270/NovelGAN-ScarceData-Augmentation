# NovelGAN — Generative Data Augmentation Framework for Scarce and Imbalanced Data

This repository implements a **novel GAN-based data augmentation framework** designed to improve classification performance under **data scarcity and class imbalance**.  
Developed as part of my **B.Tech thesis at IIT Delhi**, this project demonstrates end-to-end capabilities in **data engineering, generative modeling, and machine learning pipeline design**.

---

## 🧭 Project Overview

Modern industrial and sensor-based systems often face a shortage of labeled data, especially for minority classes.  
**NovelGAN** addresses this challenge by generating realistic synthetic data using advanced **Generative Adversarial Network (GAN)** architectures.

The framework supports both **1D signal synthesis** and **2D image-domain augmentation**, enabling robust training of classifiers in limited-data scenarios.

---

## ⚙️ Key Features

- **Multiple GAN Architectures**
  - Wasserstein GAN with Gradient Penalty (WGAN-GP)
  - Conditional WGAN for class-controlled synthesis
  - Self-Attention GAN (SAGAN) for improved spatial fidelity

- **Modular Design**
  - Independent training, generation, and evaluation scripts
  - Easy integration with external classifiers or datasets

- **Complete Data Pipeline**
  - Preprocessing (normalization, CWT conversion)
  - Synthetic data generation
  - Quality evaluation using structural metrics
  - Downstream classifier training (CNN-based)

---

## 🔒 Data Availability

The real dataset used in this project (industrial seismic footstep signals) is **private and cannot be released** due to confidentiality agreements.  
To maintain transparency and reproducibility, this repository provides:

- **Synthetic demo data** generation script for pipeline testing  
- **Open-dataset compatibility** using MNIST for demonstration  
- **Complete source code** for all models, training loops, and metrics

