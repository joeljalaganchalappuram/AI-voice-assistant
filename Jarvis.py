import random
import json
import torch
import os
from Brain import NeuralNet
from NeuralNetwork import bag_of_words , tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json","r") as json_data:
    intents = json.load(json_data)
    
FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"] 
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()


#------------------------------------------------------JARVIS--CODE's----------------------------------------------------------------------------------------------
Name = "Jarvis"

from Listen import Listen
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution

def Main():

    sentence = Listen()
    result = str(sentence)
    if sentence == "bye":
        exit()
    
    sentence = tokenize(sentence)
    x = bag_of_words(sentence,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x).to(device)
    
    output = model(x)
    
    _ , predicted = torch.max(output,dim=1)
    
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]
    
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                
                if "time" in reply:
                    NonInputExecution(reply)
             
                elif "date" in reply:
                    NonInputExecution(reply)
                
                elif "day" in reply:
                    NonInputExecution(reply)
                
                
                elif "wikipedia" in reply:
                    InputExecution(reply,result)
                
                elif "drive" in reply:
                    NonInputExecution(reply)
                
                elif "git" in reply:
                    NonInputExecution(reply)
                
                elif "college" in reply:
                    NonInputExecution(reply)
                
                elif "whatsap" in reply:
                    NonInputExecution(reply)
                
                elif "exit" in reply:
                    NonInputExecution(reply)  
                
                elif "music" in reply:
                    NonInputExecution(reply) 
                
                elif "climate" in reply:
                    NonInputExecution(reply)
                
                elif "quit" in reply:
                    NonInputExecution(reply)
                
                elif "instagram" in reply:
                    NonInputExecution(reply)
                
                elif "introduce" in reply:
                    NonInputExecution(reply)
                
                
                    
                else:
                    Say(reply)
                                 
while True:                
     Main()
     

