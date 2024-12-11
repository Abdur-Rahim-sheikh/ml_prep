# AI Engineer Written Test Preparation

## Section 1: Machine Learning

### Question 1: What is the difference between supervised, unsupervised, and reinforcement learning?  
**Answer:**
- **Supervised Learning**: Uses labeled data to train models. The model predicts outcomes based on the input data.
- **Unsupervised Learning**: Deals with unlabeled data. The model finds patterns, such as clustering or dimensionality reduction.
- **Reinforcement Learning**: Focuses on learning through interaction with an environment to maximize rewards over time.

---

### Question 2: Explain the concept of overfitting in machine learning. How can it be avoided?  
**Answer:**
- **Overfitting** occurs when a model learns the training data too well, including noise and irrelevant patterns, leading to poor performance on unseen data.
- **Avoidance**:
  - Use more training data.
  - Implement techniques like regularization (L1, L2).
  - Use cross-validation.
  - Prune decision trees or simplify models.

---

### Question 3: Write a Python function to calculate the accuracy of a machine learning model given `y_true` and `y_pred`.
```python
def calculate_accuracy(y_true, y_pred):
    correct = sum(y_t == y_p for y_t, y_p in zip(y_true, y_pred))
    return correct / len(y_true)

# Example usage:
# y_true = [1, 0, 1, 1]
# y_pred = [1, 0, 0, 1]
# print(calculate_accuracy(y_true, y_pred))
```
### Question 4: What are activation functions in neural networks? Name a few commonly used ones.
Answer: Activation functions introduce non-linearity into a neural network, enabling it to learn complex patterns. Common activation functions include:

- Sigmoid
    - $f(x) = \frac{1}{1 + e^{-x}}$
- ReLU (Rectified Linear Unit)
    - $f(x) = \max(0, x)$
- Tanh
    - $f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
- Softmax
    - $f(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}$

## Section 2: Cloud Platforms
### Question 5: What are the benefits of using cloud platforms for deploying machine learning models?
Answer:

- Scalability: Easily scale resources as per the workload.
- Cost-Effectiveness: Pay-as-you-go pricing.
- Integration: Access to tools like storage, monitoring, and APIs.
- High Availability: Minimized downtime due to redundant systems.

### Question 6: Explain the concept of serverless architecture. Give an example.
Answer:

Serverless Architecture allows you to run applications without managing infrastructure. The cloud provider automatically allocates resources.
Example: AWS Lambda lets you execute code in response to events.

### Question 7: Write a Python script to upload a file to an S3 bucket using AWS SDK (boto3).
```python
import boto3

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name or file_name)
        print("File uploaded successfully!")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Example usage:
# upload_file_to_s3('test.txt', 'my-bucket')
```
Section 3: Prompt Engineering


### Question 8: What is prompt engineering in the context of AI?
Answer: Prompt engineering involves crafting precise and effective inputs (prompts) to guide AI models like GPT to generate desired outputs. It focuses on structure, clarity, and context.

### Question 9: What are few-shot and zero-shot learning in prompt engineering?
Answer:

- Zero-shot learning: The model is tasked with solving a problem without prior examples.
    - Example: Asking a model to translate a language it hasn't seen before.
    - use case: translation, summarization
- Few-shot learning: The model is given a few examples of the task to guide its response.
    - Example: Providing a few examples of summarization to generate a summary.
    - use case: text generation, question answering

### Question 10: Write an example prompt for generating Python code that calculates the factorial of a number using recursion.
Prompt:
"Write a Python function to calculate the factorial of a number using recursion."

Output:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage:
# print(factorial(5))  # Output: 120
```

### Question 11: Provide a prompt to explain the concept of machine learning to a 12-year-old.
Prompt:
"Explain machine learning in simple terms suitable for a 12-year-old."

Output:
"Machine learning is like teaching a computer by showing it lots of examples. If you want it to recognize dogs, you show it many pictures of dogs, and it learns the patterns to identify dogs in new pictures."

## Section 4: Coding Challenges
### Question 12: Write a Python function to check if a given string is a palindrome.
```python
def is_palindrome(s):
    return s == s[::-1]

# Example usage:
# print(is_palindrome("radar"))  # True
# print(is_palindrome("hello"))  # False
```
### Question 13: Implement a simple linear regression model from scratch in Python.

```python
import numpy as np

def simple_linear_regression(X, y):
    n = len(X)
    mean_X, mean_y = np.mean(X), np.mean(y)
    b1 = sum((X - mean_X) * (y - mean_y)) / sum((X - mean_X) ** 2)
    b0 = mean_y - b1 * mean_X
    return b0, b1

# Example usage:
# X = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 4, 2, 5, 6])
# b0, b1 = simple_linear_regression(X, y)
# print(f"Intercept: {b0}, Slope: {b1}")
```
### Question 14: Write a Python function to sort a list of numbers using quicksort.
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
# print(quicksort([3, 6, 8, 10, 1, 2, 1]))
```
### Question 15: Explain the importance of data preprocessing in machine learning.
Answer: Data preprocessing ensures that data is clean, consistent, and suitable for training models. It includes steps like:

Handling missing values.
Encoding categorical data.
Normalizing or standardizing features.
Removing outliers.