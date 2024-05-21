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

    print("=" * 20)

    # 4. Create experiments
    experiment_name = "Apple_Models"

    # Provide an Experiment description that will appear in the UI
    experiment_description = (
        "This is the grocery forecasting project. "
        "This experiment contains the produce models for apples."
    )

    # Provide searchable tags that define characteristics of the Runs that
    # will be in this Experiment
    experiment_tags = {
        "project_name": "grocery-forecasting",
        "store_dept": "produce",
        "team": "stores-ml",
        "project_quarter": "Q3-2023",
        "mlflow.note.content": experiment_description,
    }

    # Create the Experiment, providing a unique name
    if old := client.get_experiment_by_name(experiment_name):
        client.delete_experiment(old.experiment_id)
    produce_apples_experiment = client.create_experiment(
        name=experiment_name, tags=experiment_tags
    )

    # 5. Searching based on tags
    apples_experiment = client.search_experiments(
        filter_string="tags.project_name = 'grocery-forecasting' AND tags.store_dept = 'produce'"
    )
    pprint(apples_experiment[0])
    print("=" * 20)
