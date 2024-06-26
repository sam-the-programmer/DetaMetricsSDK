# DetaMetricsSDK

A Python SDK for interacting with my TensorBoard alternative that runs on [Deta Space](https://deta.space).

- [DetaMetricsSDK](#detametricssdk)
  - [Installation](#installation)
  - [Usage](#usage)
    - [TensorFlow Callback](#tensorflow-callback)
    - [Base API](#base-api)

---

## Installation

```powershell
pip install detametrics
```

## Usage
- Install in Deta Space from https://deta.space/discovery/@sam-the-programmer/detametrics

- All API classes need an URL ID passed as a parameter, which can be found in the app UI.
- They also need a Deta Space App API key, which can be gotten from...
  - Click the 3 dots on the app on your Deta Space Canvas
  - Click **"Keys"**
  - Add an API Key, and input it in the box on the App UI and in your Python code as seen below

### TensorFlow Callback
Requires Tensorflow to be installed.

```python
from detametrics.tf import DetaMetricsTFCallback

# use in your keras model
model = ...
model.fit(
  ..., # other params here
  callbacks=[DetaMetricsTFCallback("MY_URL_ID", "MY_API_KEY", log_batch=True)] # if log_batch is True, it logs every batch, else only every epoch
)
```

### Base API
Get your URL id from the UI on the [Deta Space app](https://deta.space/discovery/@sam-the-programmer/detametrics).

```python
from detametrics import DetaMetrics

metrics = DetaMetrics("MY_URL_ID", "MY_API_KEY")
metrics.clear() # WARNING: clears all past metrics

metrics.set("GraphName", "LineName", 0.1)
metrics.set("GraphName", "LineName", 123.45)
metrics.set("GraphName", "LineName", 78.9)
```
