# MLE - Radar Hand Gesture Classification Exercise

The aim of this exercise is to classify hand gestures from data recorded with a FMCW radar. The Jupyter notebook [MLE_IHF_radar_gesture_sensing_exercise.ipynb](./MLE_IHF_radar_gesture_sensing_exercise.ipynb) will guide you through the development of a Convolutional Neural Network with [Pytorch](https://pytorch.org/).


## Getting Started

To participate with a local setup, a laptop with an installation of [*Anaconda*](https://www.anaconda.com/) is the most useful choice. Please install the Anaconda Distribution by following the [installation guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#) for your operating system.

Download this Gitlab [repository](https://collaborating.tuhh.de/e-3/teaching/radar_mle) as a zip folder or clone it via **Git**. Open a **Terminal** or **Anaconda Promt**.

To clone the repository execute:

```bash
git clone https://collaborating.tuhh.de/e-3/teaching/radar_mle.git
```

Navigate to the project folder:

```bash
cd radar_mle
```

With Anaconda you can manage multiple Python environments with different dependency versions. The dependencies that are required for this exercise are listed in the [environment.yaml](./environment.yaml) file. To create a new environment run:

```bash
conda env create -f environment.yaml
```

Use the following command to activate the newly created environment.

```bash
conda activate mle-radar
```

You can view the list of installed packages with

```bash
conda list
```

Start the jupyter notebook to participate in the excercise. 

```bash
jupyter notebook
``` 

A browser window with Jupyter should have opened. Click on the *MLE_IHF_radar_gesture_sensing_exercise.ipynb* file to open the exercise. You are now able to execute and edit the code cells. 

## Removing the Environment

After the course, the environment can be deleted with
```bash
conda deactivate
conda remove --name mle-radar  --all
conda clean --all
``` 