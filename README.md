SHAPESHEET 
=================
AUG 30, 2021

A package that allows for the extraction of title section from styled pdf documents.


### What is in this repository?

  - [main script](/resource/main.py) tryout main script to use packaged model for prediction
  - [model](/models)
  - [resources](/resources) contains training logs and apex repo for mixed precision if required for training
  - [shapesheet](/src/shapesheet)
  - [tests](/tests)
  

### Getting Started

  git clone https://github.com/tosi-n/shapesheet.git
  cd shapesheet/
  pip install gdown
  mkdir ./models
  gdown --id 1T8dNmCXY9Jc8NCVxh5vK042Aguufd5vN --output models.zip
  unzip models.zip -d ./models && rm models.zip
  python setup.py install



### Usage

Shapesheet was built with the use of huggingface single bert transformer architecture for concatenating and encoding multuiple title and other title formated style features. In order to predict and extract title sections efficiently from a document

    from shapesheet.prediction import predict
    title_predict, prediction_confidence = predict(Text, IsBold, IsItalic, IsUnderlined, Left, Right, Top, Bottom, FontType)






