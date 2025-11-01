from pathlib import Path
import os, numpy as np

# works in Colab and local
try:
    ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ROOT = Path(os.getcwd())

RAW_DIR = ROOT / "src" / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def generate_seismic_like_signal(length=1500,
                                 base_freq=35,
                                 noise_level=0.03,
                                 impact_prob=0.12):
    t = np.linspace(0, 1, length)
    sig = 0.3 * np.sin(2 * np.pi * base_freq * t)
    sig += 0.15 * np.sin(2 * np.pi * (base_freq / 2) * t + np.random.rand() * 2 * np.pi)
    sig += 0.05 * np.sin(2 * np.pi * (base_freq * 1.7) * t)

    impacts = np.zeros_like(sig)

    for i in range(length):
        if np.random.rand() < impact_prob:
            k = np.random.randint(5, 20)  # length of the impact
            end = min(i + k, length)      # clamp to array
            win_len = end - i
            window = np.hanning(win_len) * np.random.uniform(0.4, 0.8)
            impacts[i:end] += window

    sig += impacts
    sig += noise_level * np.random.randn(length)
    sig = np.clip(sig, -1, 1)
    return sig.astype("float32")


def main():
    # simulate imbalance
    specs = {
        "person_00": 500,
        "person_01": 200,
        "person_02": 80,
    }

    for cls, n in specs.items():
        cls_dir = RAW_DIR / cls
        cls_dir.mkdir(parents=True, exist_ok=True)
        for i in range(n):
            sig = generate_seismic_like_signal(
                base_freq=np.random.randint(25, 55),
                noise_level=np.random.uniform(0.02, 0.06),
                impact_prob=np.random.uniform(0.05, 0.15),
            )
            np.save(cls_dir / f"{cls}_{i:04d}.npy", sig)

    print("✅ Synthetic dataset created at", RAW_DIR)


if __name__ == "__main__":
    main()
