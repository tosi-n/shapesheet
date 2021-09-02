import os
import logging
# from src.shapesheet.pre_process import preprocessor
# from src.shapesheet.model import ClassificationModel
from src.shapesheet.prediction import predict
from datetime import datetime, timedelta
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(filename="./resources/training.log",level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


if __name__ == "__main__":
    pred = predict('Sales and Marketing', True, False, False, 33.1, 101.3, 66.6, 72.1, 'New Times Roman')
    print(pred)

    # train_csv = pd.read_csv("./data/train_sections_data.csv", encoding='ISO-8859-1')
    # test_csv = pd.read_csv("./data/test_sections_data.csv", encoding='ISO-8859-1')

    # preprocessor(train_csv, test_csv)

    # model = ClassificationModel(model_type='bert', model_name='/Users/lade/Documents/Dev/Side_projects/Shapesheet/models', num_labels=2, use_cuda=False, args={'num_train_epochs': 3, 'reprocess_input_data': True, "output_dir": "models", "best_model_dir": "models/best_model", "evaluate_during_training": False, 'overwrite_output_dir': True})#bert-base-uncased
    # train_df = pd.read_csv('./data/train_data.csv', sep='\t', encoding='utf-8')
    # eval_df = pd.read_csv('./data/test_data.csv', sep='\t', encoding='utf-8')

    # # Train the model
    # # logger.info('Training and evaluating model with trainset and evalset data...')
    # # model.train_model(train_df = train_df, eval_df=None, show_running_loss=True)

    # # eval_result, _, _ = model.eval_model(eval_df)
    
    # content = ['Sales and Marketing' + ' ' + str(True) + ' ' + str(False) + ' ' + str(False) + ' ' + str(33.1) + ' ' + str(101.3) + ' ' + str(66.6) + ' ' + str(72.1) + ' ' + 'New Times Roman']
    # preds_l, outputs = model.predict(content)
    # print(preds_l)

    # logger.info('Evaluation result produces an F1-SCORE of {}'.format(str(eval_result['F1-Score']*100)))