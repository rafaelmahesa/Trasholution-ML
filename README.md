# Trasholution-ML

## Github Repository for the Machine Learning side of Trasholution

### (Bangkit 2023 Capstone Project C23-PS250 Team)

- For the main repository you can go to this [repository](https://github.com/ignatiusbarry69/ALL-TRASHOLUTION)

## Model Training

### Dataset

- Datasets used to train the model can be accessed on [Google Drive](https://drive.google.com/file/d/1iNoJeuymN8SObhBQdPIcWULh9ZbE0QcR/view?usp=drive_link) and [Kaggle Dataset](https://www.kaggle.com/datasets/rafaelmahesa/waste-image-size-520).
- In this dataset there are 8 class of trash/waste type; Electronic_Waste, Food_Scraps, Glass, Metalic_Materials, Organic_Vegetation_Waste, Paper, Plastic, and Textile.
- This number of image in this dataset are split into 3 part per image class:
  - Training data : 80% of 520 images (416 images per image class).
  - Validation data : 10% of 520 images (52 images per image class).
  - Testing data : 10% of 520 images (52 images per image class).
- This dataset consist of image taken from scraping the internet.

### Jupyter Notebooks for Training Models

- At first, we develop two kind of model with version 1 created from scratch and version 2 are from transfer learning.
- From our early test we found that the version 1 only able to reach the testing accuracy of 73%, meanwhile the first complete iteration of version were able to reach testing accuracy of approx. 89%.
- Therefore we decided to drop the version 1 model to keep improving the version 2 model.
- When we first tried to develop the version 2 model, we tried to compare the result of 3 base model that is the VGG16, Inception V3, and Xception to our dataset. And we found that the with Xception as base model have the highest score out of the three.
- Jupyter notebooks used in training the model are in the [`/Training Notebooks/`](https://github.com/rafaelmahesa/Trasholution-ML/tree/main/Training%20Notebooks) folder:
  - [`training_model_waste_classification_v2_1.ipynb`](https://github.com/rafaelmahesa/Trasholution-ML/blob/main/Training%20Notebooks/training_model_waste_classification_v2_1.ipynb) used to train the `model-waste_classification-v2_1.h5` model
    - This model architecture are a little bit different from the previous model in terms of the number of hidden layer in the fully reconected layer (Dense layer).
  - [`training_model_waste_classification_v2_2.ipynb`](https://github.com/rafaelmahesa/Trasholution-ML/blob/main/Training%20Notebooks/training_model_waste_classification_v2_2.ipynb) used to train the `model-waste_classification-v2_2.h5` model
    - This model architecture differ from the previous version in terms of fine tuning the transfer learning model with the last 6 layers (the block 14 group of Xception model layers) are fine-tuned to the this dataset.

### Exported Models

- The exported model can be accessed [here](https://drive.google.com/drive/folders/1ryxlEKn-7cKjrX03jPE44BFG4yeLzKnS?usp=sharing) (Google Drive):
  - `model-waste_classification-v2.zip` (TensorFlow SavedModel format) has an accuracy score of:
    - training : 99.82%
    - validation : 89.90%
    - testing : 89.18%
  - `model-waste_classification-v2_1.h5` (Keras HDF5 format) has an accuracy score of:
    - training : 99.07%
    - validation : 89.90%
    - testing : 90.38%
  - `model-waste_classification-v2_2.h5` (Keras HDF5 format) has an accuracy score of:
    - training : 99.07%
    - validation : 92.07%
    - testing : 92.06%
- The model that is currently in use for deployment is the `model-waste_classification-v2_2.h5`.
