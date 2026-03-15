# macro_to_micro

Code and analysis for modeling emergent top-down informational influence under shared environmental constraints.

This repository accompanies the paper and provides everything needed to reproduce the figures. All simulations are self-contained, no external datasets are required.

## Repository contents

- `macro_to_micro_figs.ipynb` — Jupyter notebook that generates all main-text figures (1A, 1B, 2A, 2B, 3, 4) and supplementary figures (S1–S5)
- `figures/` — output directory for saved figures (created automatically by the notebook)

## Requirements

- Python 3.8+
- NumPy
- Matplotlib
- SciPy
- scikit-learn

Install dependencies with:

```bash
pip install numpy matplotlib scipy scikit-learn
```

## Reproducing the figures

Run the notebook from start to finish:

```bash
jupyter notebook macro_to_micro_figs.ipynb
```

Each code cell produces exactly one figure and saves it to the `figures/` directory at 300 dpi. The global random seed is fixed (`SEED = 42`), so results are fully deterministic.

<!-- ## Citation

If you use this code, please cite:

```bibtex
@article{macro_to_micro,
  title   = {},
  author  = {},
  journal = {},
  year    = {},
  doi     = {}
}
``` -->
