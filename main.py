import os
import logging
# from shapesheet.pre_process import preprocessor
# from shapesheet.model import ClassificationModel
from shapesheet.prediction import predict
from datetime import datetime, timedelta
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(filename="./resources/training.log",level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


if __name__ == "__main__":
    pred = predict('Sales and Marketing', True, False, False, 33.1, 101.3, 66.6, 72.1, 'New Times Roman')
    print(pred)
