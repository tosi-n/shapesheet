import pandas as pd
from .config.smooth import smooth_categories



def preprocessor(train_csv, test_csv):
    train_csv['text'] = train_csv['Text'] + ' '  + train_csv['IsBold'].astype(str) + ' '  + train_csv['IsItalic'].astype(str) + ' '  + train_csv['IsUnderlined'].astype(str) + ' '  + train_csv['Left'].astype(str) + ' '  + train_csv['Right'].astype(str) + ' '  + train_csv['Top'].astype(str) + ' '  + train_csv['Bottom'].astype(str) + ' '  + train_csv['FontType'].astype(str)

    train_csv.rename(columns={'Label': 'labels'},
                                inplace=True)

    label_dict = {
        0:'non_title',
        1:'title'
        }

    train_csv['Label'] = train_csv['labels'].map(label_dict)

    train_cats = {'non_title':3600,
            'title':3600}

    train_csv = smooth_categories(train_csv, train_cats, 'Label')

    train_csv = train_csv[['text', 'labels']]



    test_csv['text'] = test_csv['Text'] + ' '  + test_csv['IsBold'].astype(str) + ' '  + test_csv['IsItalic'].astype(str) + ' '  + test_csv['IsUnderlined'].astype(str) + ' '  + test_csv['Left'].astype(str) + ' '  + test_csv['Right'].astype(str) + ' '  + test_csv['Top'].astype(str) + ' '  + test_csv['Bottom'].astype(str) + ' '  + test_csv['FontType'].astype(str)

    test_csv.rename(columns={'Label': 'labels'},
                                inplace=True)

    test_csv['Label'] = test_csv['labels'].map(label_dict)

    test_cats = {'non_title':405,
            'title':405}



    test_csv = smooth_categories(test_csv, test_cats, 'Label')

    test_csv = test_csv[['text', 'labels']]

    train_csv.to_csv('./data/train_data.csv', sep='\t', encoding='utf-8', index=False, header=True)
    test_csv.to_csv('./data/test_data.csv', sep='\t', encoding='utf-8', index=False, header=True)