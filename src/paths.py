from pathlib import Path
p_root = Path(__file__).resolve().parents[2]
p_data = p_root /"data"
p_raw = p_data / "raw"
p_proc = p_data / "processed"
p_nb = p_root / "notebooks"
p_out = p_root / "outputs"

