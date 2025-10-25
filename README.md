# NovelGAN-ScarceData-Augmentation

![Deep Learning](https://img.shields.io/badge/DeepLearning-GAN%2FWGAN--GP-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)
![Commits](https://img.shields.io/badge/Update-Weekly-blueviolet)

Generative Adversarial Networks for **synthetic seismic footstep data generation** under **low-data** and **class-imbalanced** conditions.  
This work builds on my applied machine learning research at **IIT Delhi**.

---

## 🎯 Project Goals
- Generate **1D seismic signals** using **Wasserstein GAN with Gradient Penalty (WGAN-GP)**
- Convert signals to **CWT images** and augment them using **Self-Attention GAN (SAGAN)**
- Improve CNN classifier performance using realistic synthetic samples

---

## 🧠 Why It Matters
Footstep vibration signals enable non-intrusive **person identification** and **imposter detection** for security systems.  
However, collecting **large labeled datasets is difficult and expensive**.  
GAN-based augmentation offers:
- Better generalization
- Less overfitting
- Improved class coverage

---

## 🏗️ Architecture Overview

Raw Seismic Signals
↓
Preprocessing → WGAN-GP → Synthetic 1D Waveforms → CNN Classifier ↑
↓
CWT Transform → SAGAN → Synthetic Footstep Images → CNN Classifier ↑

yaml
Copy code

---

## 🗂️ Repository Structure

src/
data/ # Data loaders + CWT utilities
models/ # WGAN-GP & SAGAN architectures
train/ # Training scripts
eval/ # MED, MDSSI, SSIM evaluation
notebooks/ # Weekly development notebooks
figures/ # Generated samples & plots
requirements.txt

yaml
Copy code

---

## 🧪 Tools & Methods
| Category | Technologies |
|---------|--------------|
| Deep Learning | TensorFlow, Keras |
| Signal Processing | NumPy, SciPy, PyWavelets |
| Modeling | CNNs, WGAN-GP, SAGAN |
| Workflow | Google Colab, GitHub |

---

## 📌 Example Outputs

### ✅ Seismic Waveform (placeholder)
<img src="figures/sample_waveform.png" width="450"/>

### ✅ CWT Footstep Image (placeholder)
<img src="figures/sample_cwt.png" width="350"/>

Real generated examples will be added as training progresses.

---

## 📝 How to Run
```bash
git clone https://github.com/agrawaladitya270/NovelGAN-ScarceData-Augmentation.git
cd NovelGAN-ScarceData-Augmentation
pip install -r requirements.txt
```
---
👤 Author
Aditya Agrawal
B.Tech, IIT Delhi
Machine Learning & Signal Processing


