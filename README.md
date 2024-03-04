# Frequently asked questions
## Contents
1. [How to overcome underfitting?](#how-to-overcome-underfitting)
2. [How to overcome overfitting?](#how-to-overcome-overfitting)
3. [How KNN differs from k-means clustering?](#how-knn-differs-from-k-means-clustering)

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
