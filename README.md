# Deepfake Detection

A deep learning project that detects whether a face image or video frame is **real or AI-generated (deepfake)** using a TensorFlow-based convolutional neural network.

This project explores how modern computer vision models can identify artifacts and inconsistencies introduced by synthetic media generation.

---

## Overview

Deepfakes are AI-generated media where a person’s face or voice is manipulated to create realistic but fake content. Detecting deepfakes is becoming increasingly important in areas such as:

* Media verification
* Cybersecurity
* Social media moderation
* Digital forensics

This project builds a **deepfake detection model using TensorFlow**, trained to classify images as **REAL or FAKE**.

The model learns subtle visual artifacts commonly introduced by deepfake generation techniques such as:

* Face warping
* Blending artifacts
* Texture inconsistencies
* Compression anomalies

Research in this area often relies on deep learning models that analyze spatial and temporal cues in images or videos to detect manipulation. ([GitHub][1])

---

# Model Performance

The model was trained for **20 epochs** and achieved the following results:

```
Epoch 20/20
39/39 [==============================]
loss: 0.0478
accuracy: 0.9840

val_loss: 0.0258
val_accuracy: 0.9943
```

### Final Metrics

| Metric              | Score      |
| ------------------- | ---------- |
| Training Accuracy   | **98.40%** |
| Validation Accuracy | **99.43%** |
| Training Loss       | **0.0478** |
| Validation Loss     | **0.0258** |

These results demonstrate strong performance on the validation dataset, indicating the model successfully learned features that distinguish real and manipulated media.

---

# Model Architecture

The model is implemented in **TensorFlow/Keras** and follows a CNN-based architecture designed for image classification tasks.

General pipeline:

```
Input Image
     ↓
Preprocessing
     ↓
Convolutional Layers
     ↓
Feature Extraction
     ↓
Fully Connected Layers
     ↓
Sigmoid Output
     ↓
Real / Fake Classification
```

Key components include:

* Convolution layers for spatial feature extraction
* Pooling layers for dimensionality reduction
* Dense layers for classification
* Sigmoid activation for binary prediction

---

# Dataset

The model is trained on a dataset containing **real and deepfake images**.

Typical dataset structure:

```
dataset/
   real/
      img1.jpg
      img2.jpg
   fake/
      img1.jpg
      img2.jpg
```

Each image is labeled:

* **0 → Real**
* **1 → Fake**

Data preprocessing includes:

* Image resizing
* Normalization
* Train/validation splitting

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Rediett/Deepfake-Detection.git
cd Deepfake-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Training the Model

Run the training script:

```bash
python train.py
```

Training will:

1. Load and preprocess the dataset
2. Train the CNN model
3. Evaluate validation performance
4. Save the trained model

---

# Running Predictions

To test the model on new images:

```bash
python predict.py --image path/to/image.jpg
```

Output example:

```
Prediction: FAKE
Confidence: 97.3%
```

---

# Project Structure

```
Deepfake-Detection
│
├── dataset/            # Training dataset
├── models/             # Saved trained models
├── train.py            # Model training script
├── predict.py          # Inference script
├── requirements.txt    # Python dependencies
└── README.md
```

---

# Future Improvements

Possible enhancements include:

* Training on larger datasets
* Adding video-based detection
* Using transfer learning (EfficientNet / Xception)
* Implementing attention mechanisms
* Improving generalization across different deepfake generators

---

# Applications

This project can be used for:

* Deepfake research
* Digital media verification
* AI ethics projects
* Machine learning portfolio demonstrations

---

# License

This project is released under the **MIT License**.
