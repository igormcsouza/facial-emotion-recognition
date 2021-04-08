# Research

## Manage the project packages

On this research, the packages is been managed using
[poetry](https://python-poetry.org/). The documentation is very good and
complete. First thing, before doing any command on this readme, install the
packages related.

```bash
FacialEmotionRecognition/research$ poetry install
```

## Preprocessing Data Script

The data on the repository is not prepare to be used by Keras data generator.
The script `data_preprocessing.py` will organize the images on the way Keras
like things. See the [documentation](https://keras.io/api/preprocessing/image/)
for more information on this matter.

Use the script running the command like below.

```bash
FacialEmotionRecognition/research$ poetry run data_preprocessing.py
```
