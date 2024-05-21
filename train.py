from mlflow import MlflowClient
from pprint import pprint
from sklearn.ensemble import RandomForestRegressor

if __name__ == "__main__":
    # 1. Tracking Server 연결: Tracking Server와 상호작용하여 데이터를 송수신
    client = MlflowClient(tracking_uri="http://127.0.0.1:8080")

    # 2. Search existing experiments
    all_experiments = client.search_experiments()
    pprint(all_experiments)
    # 3. Get default experiments
    default_experiment = [
        {"name": experiment.name, "lifecycle_stage": experiment.lifecycle_stage}
        for experiment in all_experiments
        if experiment.name == "Default"
    ][0]
    print(default_experiment)
