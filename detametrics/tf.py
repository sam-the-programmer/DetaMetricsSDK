import tensorflow as tf
import multiprocessing as mp
from .sdk import DetaMetrics

def background(queue: mp.Queue, backend: DetaMetrics):
    while True:
        metric, value, mode = queue.get()
        backend.set(metric, mode, value)

class DetaMetricsTFCallback(tf.keras.callbacks.Callback):
    def __init__(self, urlId: str, apiKey: str, log_batch: bool=False) -> None:
        self.__deta_backend = DetaMetrics(urlId, apiKey)
        self.__log_batch = log_batch
    
    def on_train_begin(self, logs=None):
        self.__queue = mp.Queue()
        self.__process = mp.Process(target=background, args=(self.__queue, self.__deta_backend))
        self.__process.start()
    
    def on_train_end(self, logs=None):
        self.__process.terminate()
        self.__process.join()
    
    def on_train_batch_end(self, batch, logs=None):
        if self.__log_batch:
            for metric, value in logs.items():
                if metric.startswith("val_"):
                    self.__queue.put((metric[4:], value, "Validation"))
                else:
                    self.__queue.put((metric, value, "Training"))

    def on_epoch_end(self, epoch, logs=None):
        for metric, value in logs.items():
            if metric.startswith("val_"):
                self.__queue.put((metric[4:], value, "Validation"))
            else:
                self.__queue.put((metric[4:], value, "Validation"))
