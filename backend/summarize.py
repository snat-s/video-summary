}import sys
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
nltk.download('punkt')

checkpoint = "sshleifer/distilbart-cnn-12-6"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

def summarize(text_name):
    with open(text_name, "r") as f:
        texto = f.read()


    sentences = nltk.tokenize.sent_tokenize(texto)

    #print(summarizer.model_max_length )
    print(max([len(tokenizer.tokenize(sentence)) for sentence in sentences]))

    # create chunks
    # initialize
    length = 0
    chunk = ""
    chunks = []
    count = -1
    for sentence in sentences:
      count += 1
      combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

      if combined_length  <= tokenizer.max_len_single_sentence: # if it doesn't exceed
        chunk += sentence + " " # add the sentence to the chunk
        length = combined_length # update the length counter

        # if it is the last sentence
        if count == len(sentences) - 1:
          chunks.append(chunk.strip()) # save the chunk

      else:
        chunks.append(chunk.strip()) # save the chunk

        # reset
        length = 0
        chunk = ""

        # take care of the overflow sentence
        chunk += sentence + " "
        length = len(tokenizer.tokenize(sentence))
    print(len(chunks))

    # inputs to the model
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

    summary = []
    for input in inputs:
      output = model.generate(**input)
      summary.append(tokenizer.decode(*output, skip_special_tokens=True))

    return summary

if __name__ == "__main__":
    file_text = sys.argv[1]
    summarize(file_text)
