# Second Code: Character-Level RNN Classification

This notebook follows PyTorch's NLP-from-scratch tutorial and trains a character-level recurrent neural network to predict the language of origin of a surname.

## Setup

Both tutorials share the root Python 3.12 environment. From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Set-Location '.\Second Code'
jupyter notebook char_rnn_classification_tutorial.ipynb
```

In VS Code, select the root `.venv` as the notebook kernel.

## Data

The notebook expects the PyTorch tutorial names dataset under `data/names`. The local dataset is excluded from Git. To recreate it, download `https://download.pytorch.org/tutorial/data.zip` and extract it inside `Second Code`.

## Dependencies

The notebook uses PyTorch, NumPy, Matplotlib, and Python standard-library modules. These dependencies are already included in the root `requirements.txt` and `.venv`.
