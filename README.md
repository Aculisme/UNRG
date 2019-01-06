## UN Resolution Generator
By [Aculisme](https://github.com/aculisme)

Built for Reddit, on top of Textgenrnn by [Minimaxir](https://github.com/minimaxir).

# Instructions:
* (Optional) create a Virtual Environment in which to install the required libraries
* Install Tensorflow and Textgenrnn via pip. You may need to perform this manually with help from StackOverflow if on Mac.
* Run `gather.py` in order to generate a list of comments to use as inputs. The resulting file can be found in the `inputs` folder.
* Run `train.py` to train the RNN. The resulting file can be found in the `models` folder.
* Run `generate.py` to produce a list of RNN-generated comments. The resulting file can be found in the `outputs` folder. There is a possibility of the 