from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

def train_model(df_final, target_column='win'):
    """
    Train a logistic regression model on the provided DataFrame.

    Parameters:
    df_final (DataFrame): DataFrame containing the features and target column.
    target_column (str): The name of the target variable column.

    Returns:
    tuple: A tuple containing the trained model and the test set for evaluation.
    """
    np.random.seed(10)
    X = df_final.drop(target_column, axis=1)
    Y = df_final[target_column].values
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    model_lr = LogisticRegression()
    model_lr.fit(x_train, y_train)
    
    return model_lr, (x_test, y_test)

def predict_and_evaluate(model, test_set):
    """
    Make predictions with the trained model and evaluate its accuracy.

    Parameters:
    model: The trained model.
    test_set (tuple): A tuple containing the test features and target.

    Returns:
    float: The accuracy of the model on the test set.
    """
    x_test, y_test = test_set
    y_pred = model.predict(x_test)
    print(y_pred)  # Print predictions
    acc = accuracy_score(y_test, y_pred)
    
    return acc
