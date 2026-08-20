# First Code: FGSM Adversarial Example Tutorial

This project contains a runnable PyTorch notebook demonstrating the Fast Gradient Sign Method (FGSM) attack against an MNIST classifier.

## Setup

The project uses Python 3.12 and a virtual environment in `.venv`.

From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Set-Location '.\First Code'
jupyter notebook fgsm_tutorial.ipynb
```

In VS Code, open `fgsm_tutorial.ipynb` and select `.venv` as the notebook kernel.

## Running the notebook

Run the cells from top to bottom. MNIST is downloaded automatically into `data/`.

The original tutorial expected `data/lenet_mnist_model.pth`, but its external download link is no longer available. If the file is missing, the notebook now trains a replacement model for one epoch and saves it at that path. This is a one-time CPU setup; later runs load the cached weights directly.

The `data/` directory and virtual environment are ignored by Git because both can be recreated.

## Dependencies

- PyTorch and torchvision
- NumPy
- Matplotlib
- Jupyter and ipykernel

See the root `requirements.txt` for the installable dependency list.
