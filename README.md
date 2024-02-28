# Frequently asked questions
## Contents
1. [How to overcome underfitting?](#how-to-overcome-underfitting)
2. [How to overcome overfitting?](#how-to-overcome-overfitting)

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

