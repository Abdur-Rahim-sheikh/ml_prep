# Frequently asked questions
## Contents
1. [How to overcome underfitting?](#how-to-overcome-underfitting)
2. [How to overcome overfitting?](#how-to-overcome-overfitting)
3. [How KNN differs from k-means clustering?](#how-knn-differs-from-k-means-clustering)
4. [Explain how a ROC curve works.](#explain-how-a-roc-curve-works)
5. [Define precision and recall.](#define-precision-and-recall)
6. [What is Naive Bayes’ Theorem?](#what-is-naive-bayes-theorem)
7. [What is ensemble learning technique?](#what-is-ensemble-learning-technique)
8. [What’s the “kernel trick” and how is it useful?](#whats-the-kernel-trick-and-how-is-it-useful)

### How to overcome underfitting?
1) Increase Model Complexity
    - Use more complex model architectures that can capture the underlying patterns in the data more effectively.
2) Feature Engineering
    - Enhance the model input with additional features or transform existing features to improve model learning capacity.
3) Reduce Regularization
    - If regularization is applied, reducing its strength can allow the model to fit the training data more closely.
4) More Training Data
    - Increasing the amount of training data can help the model to learn the underlying patterns more effectively.

also...
- Reduce Dropout
- Increase the number of layers and neurons in the neural network. (which is increasing the model complexity)
- Increase the number of epochs

### How to overcome overfitting?
1) Simplify Model
    - Use a less complex model to prevent the model from capturing noise in the training data.
2) Cross-Validation
    - Use cross-validation techniques to ensure that the model generalizes well to unseen data.
3) Regularization Techniques
    - Apply regularization methods (like L1, L2 regularization) to penalize large weights and prevent the model from fitting the training data too closely.
4) Data Augmentation
    - In the context of image, text, or audio data, augmenting the dataset can help increase its diversity, leading to better generalization.

### How KNN differs from k-means clustering?
- [KNN](supervised_algorithm/KNN.ipynb) is supervised learning where [k-means clustering](unsupervised_algorithm/k_means_clustering.ipynb) is unsupervised learning
- if we give a test value to knn, it get distance with all train values then sorts it. Then it takes k nearest values and get the most frequent value from them.
- on the other hand, k-means clustering get the distance of trained k-centroids with the test data and choses the nearest centroid to assign the test data to that cluster.
- The critical difference here is that KNN needs labeled points and is thus supervised learning, while k-means doesn’t—and is thus unsupervised learning.

### Explain how a ROC curve works.
- ROC curve is a graphical representation of the trade-off between the true positive rate (TPR) and false positive rate (FPR) for a binary classification system as its discrimination threshold is varied. It is also called trade-off between the sensitivity of the model (true positives) vs the fall-out or the probability it will trigger a false alarm (false positives).

<img src="static/roc.png" alt="ROC formula and graph"
    height="350px" width="700px" style="filter: brightness(70%);">


### Define precision and recall.
- Precision and recall are two fundamental metrics for evaluating the performance of classification models. They are defined as follows:
    - Precision: The ratio of correctly predicted positive observations to the total predicted positive observations. It is also called Positive Predictive Value (PPV).
    - Recall: The ratio of correctly predicted positive observations to the all observations in actual class. It is also called True Positive Rate or Sensitivity.

    - Precision = TP / (TP + FP)
    - Recall = TP / (TP + FN)

    - Precision and recall are inversely related. As precision increases, recall falls and vice-versa. This is called the precision-recall trade-off.

### What is Naive Bayes’ Theorem?
- Naive Bayes is a classification algorithm for binary (two-class) and multi-class classification problems. It is based on Bayes’ theorem with the assumption of independence between every pair of features. Naive Bayes is a simple and effective algorithm for classification tasks.

P(A|B) = P(B|A) * P(A) / P(B)

follow the link to understand bayes theorem in detail: [Bayes Theorem](https://youtu.be/71oNiqPoKD8?si=ez8u-InIIzaWpVxx)

![bayes theorem](static/bayes_krish_nayek.png)

### What is ensemble learning technique?
- Ensemble learning is a machine learning paradigm where multiple models (often called “weak learners”) are trained to solve the same problem and combined to get better results. The main hypothesis is that when weak models are correctly combined, they can outperform a single powerful model.

    - **Bagging**: Training multiple individual models in a parallel way. Each model is trained by a random subset of the data.
    - **Boosting**: Training multiple individual models in a sequential way. Each individual model learns from the mistakes of the previous model.
    - **Stacking**: Training multiple individual models and combine them by training a meta-model to output predictions based on the multiple models’ predictions.

    - **Random Forest**: Random Forest is an ensemble learning method that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.
    - **Gradient Boosting**: Gradient Boosting is a machine learning technique for regression and classification problems, which produces a prediction model in the form of an ensemble of weak prediction models, typically decision trees.

### What’s the “kernel trick” and how is it useful?
- The kernel trick is a method of using a linear classifier to solve a non-linear problem. It transforms the linearly inseparable data into linearly separable data by adding a new dimension to the feature space. This new dimension is called the kernel trick. The kernel trick is useful because it allows us to use linear classifiers to solve non-linear problems.
the formula for the kernel trick is:
    - K(x, y) = (x . y + 1)^d
    - where d is the degree of the polynomial kernel.
name of some kernels:
    - Linear Kernel -> K(x, y) = x . y
    - Polynomial Kernel -> K(x, y) = (x . y + 1)^d
    - Gaussian Kernel -> K(x, y) = exp(-||x - y||^2 / 2 * sigma^2)
    - Sigmoid Kernel -> K(x, y) = tanh(x . y + r)
