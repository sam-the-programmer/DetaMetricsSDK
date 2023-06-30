import tensorflow as tf
from .sdk import DetaMetrics

class DetaMetricsTFCallback(tf.keras.callbacks.Callback):
    def __init__(self, urlId: str) -> None:
        self.deta_backend = DetaMetrics(urlId)

    def on_epoch_end(self, epoch, logs=None):
        for metric, value in logs.items():
            if metric.startswith("val_"):
                self.deta_backend.set(metric[4:], "Validation", value)
            else:
                self.deta_backend.set(metric, "Training", value)
