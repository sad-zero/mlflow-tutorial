# mlflow-tutorial
[MLflow Tutorial](https://mlflow.org/docs/latest/getting-started/logging-first-model/index.html) 수행

## Tracking Server
### Setup
1. `pip install mlflow`
2. `mlflow server --host 127.0.0.1 --port 8080`
### UI
#### Experiments
- 학습된 모델들에 대한 테스트 수행
- Classic ML, LLM에 대한 테스트 수행 가능
#### Models
> 모델 메타 데이터에 모델을 연결하려면 별도 작업을 수행해야 한다.
- Model Registry 관리
- 모델 메타데이터 생성, 태깅, 버전 관리

## Client API
- 모델 학습을 위해 사용하는 주요 기능
- Tracking Server로 시각화 가능

### Default Experiment
- 실험을 명시적으로 정의하지 않고 수행한 경우, 선택되는 실험
- 실험에 대한 모든 정보를 담고 있다.
- Tracking data가 소실되는 것을 방지하기 위해 존재하는 매커니즘

### Metadata
- Client API에서 반환하는 대부분의 값은 Task 수행과 관련된 메타 데이터를 포함한다.
- Ex. `search_experiments() -> PagedList[Experiment]`
  ```python
  class Experiment(_MlflowObject):
    DEFAULT_EXPERIMENT_NAME = "Default"
    def __init__(
        self,
        experiment_id,
        name,
        artifact_location,
        lifecycle_stage,
        tags=None,
        creation_time=None,
        last_update_time=None,
    ):
        ...
  ```
