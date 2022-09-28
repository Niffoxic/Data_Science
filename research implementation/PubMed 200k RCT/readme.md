# PubMed 200k RCT
link - https://arxiv.org/abs/1710.06071

## Description 
This notebook is a replica model of the research PubMed 200k RCT.
The model summarizes a large document into five categorical classes (Background, Methods, Objectives, Conclusion, and Result) making the document easier to read.

`For further details or research works read` https://arxiv.org/pdf/1710.06071.pdf

## Contents 

**There are four models trained for each separate part of the model and one combined (complete replica) model-**
`Epochs - 10, Model [0, 1, 2, 3, 4] trained on 10% of data, Model 5 trained on full dataset.`

* Model 0 - This model is a baseline model for comparing other model progress `(Accuracy 71.66%)`.
* Model 1 - This model replicates the token embedding model from the research paper `(Accuracy 75.35%)`.
* Model 2  - This model is same as "Model 1" but with transfer learning for token vectorization (tfh model - https://tfhub.dev/google/universal-sentence-encoder/4) `(Accuracy 76.49%)`.
* Model 3  - This model replicates the character embedding model from the research paper `(Accuracy 74.01%)`.
* Model 4 - This model concatenate model 3 and 2  and trains upon them ( the lower part of the model) `(Accuracy 74.013%)`.
* Model 5 - The complete replica of the model architecture ( https://arxiv.org/pdf/1612.05251.pdf ) `(Accuracy 86.30%)`.


## Credits
**Thanks to**
* Franck Dernoncour MIT francky@mit.edu 
* Ji Young Lee MIT jjylee@mit.edu
* Peter Szolovits MIT psz@mit.edu

for the `research, dataset and neural network model architecture :)`
