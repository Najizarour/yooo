# Machine Learning Tutorials

This repository contains PyTorch tutorials that share one Python 3.12 virtual environment.

## Projects

- `First Code/fgsm_tutorial.ipynb` — FGSM adversarial examples on MNIST.
- `Second Code/char_rnn_classification_tutorial.ipynb` — surname-language classification with a character-level RNN.
- `Third Code/mario_rl_tutorial.ipynb` — Deep Q-learning with a Super Mario Bros environment.

## Shared environment

From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Set-Location '.\Third Code'
jupyter notebook mario_rl_tutorial.ipynb
```

In VS Code, select the root `.venv` interpreter as the notebook kernel.

## Dependencies

In addition to PyTorch, NumPy, and Matplotlib, this tutorial uses:

- Gym 0.26
- `nes-py`
- `gym-super-mario-bros`
- TorchRL and TensorDict

These are included in the root `requirements.txt`.

## Training output

The Mario notebook trains for 40 episodes and may take a while on CPU. Logs, plots, replay-buffer files, and model checkpoints are written under `checkpoints/`.

On Windows, the replay buffer is explicitly disk-backed under the run's checkpoint directory to avoid exhausting the system page file.

Generated datasets, cached models, and the virtual environment are excluded from Git and can be recreated.
