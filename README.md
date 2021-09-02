SHAPESHEET 
=================
AUG 30, 2021

A package that allows for the extraction of title section from styled pdf documents.


### What is in this repository?

  - [shapesheet](/src/shapesheet)
  - [resources](/resources) contains training logs and apex repo for mixed precision if required for training
  - [example script](/resource/example.py) tryout example script

### Getting Started

  pip install torch==1.7.1+cu110 -f https://download.pytorch.org/whl/torch_stable.html

  git clone git@bitbucket.org:logicallydevs/rep_sampling.git

  cd rep_sampling/
  
  python setup.py install



### Usage

Representative sampling was built with the use of sentence transformer for encoding and faissIndex for indexing embeddings. This helps produce a representative sample by using textual similarity search from a pool of un annotated data mapped from a query set of previously annotated data. This high-level process of using Representative sampling algorithm follows the below pattern.

  - Initialize repSampling class, which embeds the pool data
  - Train the faissIndex with train()
  - Save trained model with save()
  - Load already trained model with load()
  - Extract unlabelled pool data using textual similarity with function search_pool()



##### Example

If you are running this file for the first time, you will need to build a FAISS index. For subsequent runs, the FAISS index can be loaded from the resource filepath. The most important command-line arguments to worry about are:

  - --model-name: sentence transformer pretrained model for extracting word embedding from pool and query data.
  - --index-filepath: path to the FAISS index. If building an index, this is where it will be saved; if loading an index, this is where it will be loaded from.
  - --querydata-path: the query data set of previously labeled or groundtruth data.
  - --pooldata-path: the pool data set of unlabeled or low decision boundary data.
  - --target-col: the the target class from text clasification data required for representative sampling.
  - --class-sample-size: target class sample size to be extracted from each category.
  - --outpool-path: the export filepath for final selected representative pool from pool data.




