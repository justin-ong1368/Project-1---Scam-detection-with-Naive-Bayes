# Project-1---Scam-detection-with-Naive-Bayes

The goal is to implement a Naive Bayes model to detect scam (phishing/spam) SMS messages based on textual content.

## Project Overview

Scam messages (aka "smishing") are designed to trick recipients into revealing personal information or downloading malware. We aim to classify SMS messages as either:

- **Scam** (label: `1`)
- **Non-malicious** (label: `0`)

The classification is performed using a **Multinomial Naive Bayes** model trained on preprocessed text data.

The project involves:
- Building a **supervised Naive Bayes model**
- Evaluating its performance on a test set
- Extending it via **semi-supervised learning**
- Analyzing model behavior and word distributions

## Dataset Description

The SMS dataset is derived from the **SMS Phishing Dataset** (Mishra & Soni, 2022). It consists of three CSV files:

| File                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `sms_supervised_train.csv` | Labelled training set with `textOriginal`, `textPreprocessed`, and `class`. |
| `sms_unlabelled.csv`       | Unlabelled data used for semi-supervised learning.                        |
| `sms_test.csv`             | Labelled test data used for evaluation.                                   |

Each message has:
- `textOriginal`: raw SMS message text
- `textPreprocessed`: processes SMS message text (used for training/testing)
- `class`: binary label (`0` = non-malicious, `1` = scam)

## Tasks and Structure

The assignment is divided into four key parts:

1. **Supervised Learning**
   - Train a Naive Bayes model on the supervised dataset.
   - Analyze priors and most predictive words.

2. **Evaluation**
   - Predict labels for test data.
   - Report accuracy, precision, recall, and confidence scores.

3. **Semi-Supervised Extension**
   - Extend the model using either:
     - **Label propagation** (self-training with unlabelled data), or
     - **Active learning** (select and label a subset of unlabelled data)

4. **Comparison and Discussion**
   - Compare performance between supervised and semi-supervised models.
   - Analyze how word distributions or confidence change.

## Notes

- Only `textPreprocessed` is used for feature extraction.
- Out-of-vocabulary words in test data are ignored.
- Laplace smoothing is applied to prevent zero probabilities.

## 📚 Reference

> Mishra, S. & Soni, D. (2022). *SMS Phishing Dataset for Machine Learning and Pattern Recognition*. Mendeley Data. [https://doi.org/10.17632/f45bkkt8pr.1](https://doi.org/10.17632/f45bkkt8pr.1)