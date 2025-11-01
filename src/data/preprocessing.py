from pathlib import Path
import os, numpy as np, pywt

# handle colab
try:
    ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ROOT = Path(os.getcwd())

RAW_DIR = ROOT / "src" / "data" / "raw"
PROC_DIR = ROOT / "src" / "data" / "processed"
PROC_DIR.mkdir(parents=True, exist_ok=True)


def load_all_npy_recursive(raw_dir):
    signals, labels = [], []
    class_dirs = sorted([p for p in raw_dir.glob("*") if p.is_dir()])
    if not class_dirs:
        print(f"No class folders in {raw_dir}. Run make_synthetic.py first.")
        return None, None, None

    for lid, cls_dir in enumerate(class_dirs):
        for f in sorted(cls_dir.glob("*.npy")):
            x = np.load(f)
            if x.ndim == 1:
                x = x[:, None]
            signals.append(x)
            labels.append(lid)

    if len(signals) == 0:
        print("No .npy files found in subfolders of", raw_dir)
        return None, None, None

    signals = np.stack(signals, axis=0)
    labels = np.array(labels, dtype=np.int32)
    class_names = np.array([p.name for p in class_dirs])
    print("Loaded:", signals.shape, "labels:", labels.shape)
    return signals, labels, class_names


def minmax_to_unit(x, low=-1.0, high=1.0):
    xmin, xmax = x.min(), x.max()
    if xmax == xmin:
        return x
    return (x - xmin) / (xmax - xmin) * (high - low) + low


def signals_to_cwt(signals, wavelet="morl", scales=56):
    if signals.ndim == 3:
        signals = signals[..., 0]
    out = []
    widths = np.arange(1, scales + 1)
    for s in signals:
        cwtmatr, _ = pywt.cwt(s, widths, wavelet)
        out.append(cwtmatr)
    return np.stack(out, axis=0)


def main():
    signals, labels, class_names = load_all_npy_recursive(RAW_DIR)
    if signals is None:
        return

    # 1) normalize
    signals_minmax = minmax_to_unit(signals)
    np.save(PROC_DIR / "signals_minmax.npy", signals_minmax)
    np.save(PROC_DIR / "labels.npy", labels)
    np.save(PROC_DIR / "class_names.npy", class_names)
    print("✅ saved normalized signals, labels, class_names")

    # 2) standardized
    mean = signals.mean()
    std = signals.std() + 1e-6
    signals_std = (signals - mean) / std
    np.save(PROC_DIR / "signals_standardized.npy", signals_std)
    print("✅ saved standardized signals")

    # 3) CWT
    cwt_batch = signals_to_cwt(signals_minmax, wavelet="morl", scales=56)
    np.save(PROC_DIR / "signals_cwt.npy", cwt_batch)
    print("✅ saved CWT signals")


if __name__ == "__main__":
    main()
