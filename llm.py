from transformers import  GPT2LMHeadModel, GPT2Tokenizer
import torch
import text2emotion
import nltk

nltk.download('punkt') # resource for tokenization

model_name = "microsoft/DialoGPT-medium"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name) # load the tokenizer converts phrases in to adecuate input for the model
model = GPT2LMHeadModel.from_pretrained(model_name,output_hidden_states=True) # load the model
tokenizer.add_special_tokens({'pad_token': '[PAD]'}) # add special token for padding in case sizings arent the same


# Function to get a format that the model can process
def get_embedding(query):
    # Tokenize the query in tensors (multidimensional arrays) in pytorch format
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model(**inputs)
    
    # Extract hidden states (a tuple of (layer_0, layer_1, ..., layer_n))
    hidden_states = outputs.hidden_states  # This is a tuple of layer-wise hidden states
    
    # Get the last hidden state (or average across layers if needed)
    last_hidden_state = hidden_states[-1]
    
    # Mean pooling over the token embeddings to get the sentence embedding
    query_embedding = last_hidden_state.mean(dim=1)  # Mean of token embeddings

    return query_embedding





def generate_response(query):
    # Encode the query into tokens
    input_ids = tokenizer.encode(query, return_tensors="pt")

    # Generate a response using the model
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)
    
    # Decode and return the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Swap placeholder with input query
query = "This is great"
response = generate_response(query)
query_embedding = get_embedding(query)


emotions = text2emotion.get_emotion(query)

print(query_embedding)
print(response)
print(emotions)
print(list(emotions.values()))
