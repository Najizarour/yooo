# Third Code: Mario Reinforcement Learning

This notebook follows PyTorch's Mario reinforcement-learning tutorial. It builds a Deep Q-Network agent and trains it in the `SuperMarioBros-1-1-v0` NES environment.

## Setup

All tutorials share the Python 3.12 environment at the repository root. From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Set-Location '.\Third Code'
jupyter notebook mario_rl_tutorial.ipynb
```

In VS Code, select the root `.venv` as the notebook kernel.

## Dependencies

In addition to PyTorch, NumPy, and Matplotlib, this tutorial uses:

- Gym 0.26
- `nes-py`
- `gym-super-mario-bros`
- TorchRL and TensorDict

These are included in the root `requirements.txt`.

## Training output

The notebook trains for 40 episodes and may take a while on CPU. Logs, plots, replay-buffer files, and model checkpoints are written under `checkpoints/`. That directory is ignored by Git because its contents are generated and can become large.

On Windows, the replay buffer is explicitly disk-backed under the run's checkpoint directory to avoid exhausting the system page file.
