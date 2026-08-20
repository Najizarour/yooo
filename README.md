# Machine Learning Tutorials

This repository contains two PyTorch tutorials that share one Python 3.12 virtual environment.

## Projects

- `First Code/fgsm_tutorial.ipynb` — FGSM adversarial examples on MNIST.
- `Second Code/char_rnn_classification_tutorial.ipynb` — surname-language classification with a character-level RNN.

## Shared environment

From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

In VS Code, select the root `.venv` interpreter as the kernel for both notebooks. Run each notebook from its own project folder so relative `data/` paths resolve to that tutorial's dataset.

Generated datasets, cached models, and the virtual environment are excluded from Git and can be recreated.
