
# footstep-seismic-GAN-augmentation

This repository investigates **multi-class classification with scarce and imbalanced seismic datasets**
using **GAN-based data augmentation** techniques.

### Key Goals
- Generate synthetic 1D footstep seismic signals (WGAN-GP)
- Convert signals to CWT image domain and augment data (SAGAN)
- Improve CNN classifier performance on limited real samples

### Directory Structure
src/
data/ # dataset loading, preprocessing
models/ # GAN architectures (WGAN-GP, SAGAN)
train/ # training pipelines
eval/ # metric evaluation (MED, MDSSI, SSIM)
notebooks/ # iterative experiment development
figures/ # results, generated signal visuals
docs/ # diagrams, project notes, references

### Status (as of Week 1)
✅ Repository created  
✅ Project structure initialized  
⬜ WGAN-GP code  
⬜ Generated samples  
⬜ Classifier evaluation  
⬜ Full documentation  

---

### Author
Aditya Agrawal  
B.Tech, IIT Delhi  

