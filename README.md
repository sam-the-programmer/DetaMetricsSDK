# DetaMetricsSDK

A Python SDK for interacting with my TensorBoard alternative that runs on [Deta Space](https://deta.space).

## Installation

```powershell
pip install detametrics
```

## Usage

### TensorFlow Callback
Requires Tensorflow to be installed.

```python
from detametrics.tf import DetaMetricsTFCallback

# use in your keras model
model = ...
model.fit(
  ..., # other params here
  callbacks=[DetaMetricsTFCallback("MY_URL_ID")]
)
```

### Base API
Get your URL id from the UI on the [Deta Space app](https://deta.space/discovery/@sam-the-programmer/detametrics).

```python
from detametrics import DetaMetrics

metrics = DetaMetrics("MY_URL_ID") # get it from the Deta Space App UI
metrics.clear() # WARNING: clears all past metrics

metrics.set("GraphName", "LineName", 0.1)
metrics.set("GraphName", "LineName", 123.45)
metrics.set("GraphName", "LineName", 78.9)
```
