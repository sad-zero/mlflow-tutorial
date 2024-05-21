import mlflow
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from dataset import generate_apple_sales_data_with_promo_adjustment

if __name__ == "__main__":
    # 1. fluent API를 사용하도록(Global Handling)
    tracking_server_uri = "http://127.0.0.1:8080"
    mlflow.set_tracking_uri(tracking_server_uri)
    # 2. Active Experiment 선택
    experiment_name = "Apple_Models"
    apple_experiment = mlflow.set_experiment(experiment_name)
    # 3. Run & Artifact(학습된 모델) 경로 지정
    run_name = "apples_rf_test"
    artifact_path = "rf_apples"

    # 4. Prepare data
    data = generate_apple_sales_data_with_promo_adjustment()
    X = data.drop(columns=["date", "demand"])
    y = data["demand"]
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    params = {
        "n_estimators": 100,
        "max_depth": 6,
        "min_samples_split": 10,
        "min_samples_leaf": 4,
        "bootstrap": True,
        "oob_score": False,
        "random_state": 888,
    }
    # 5. Train
    rf = RandomForestRegressor(**params)
    rf.fit(X_train, y_train)

    # 6. Validation
    y_pred = rf.predict(X_val)
    mae = mean_absolute_error(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_val, y_pred)

    # 7. Update MLflow run context
    metrics = {"mae": mae, "mse": mse, "rmse": rmse, "r2": r2}
    with mlflow.start_run(run_name=run_name) as run:
        # 7-1. Model Parameter 저장
        mlflow.log_params(params)
        # 7-2. Metrics 저장
        mlflow.log_metrics(metrics)
        # 7-3. 학습된 모델 저장
        mlflow.sklearn.log_model(
            sk_model=rf, input_example=X_val, artifact_path=artifact_path
        )
