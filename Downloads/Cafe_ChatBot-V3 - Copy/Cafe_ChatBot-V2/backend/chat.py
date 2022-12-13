from datetime import datetime
import random
import json
import random
import torch
from backend.model import NeuralNet
from backend.nltk_utils import bag_of_words, tokenize
from src import views
from src.models import Order, Kitchen_Order

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('backend/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "backend/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"
print("Let's chat! (type 'quit' to exit)")

def chat(request):

    while True:
        # sentence = "do you use credit cards?"
        sentence = request.POST.get('input',False)
        if sentence == "quit":
            break
        elif sentence == "gpay" or "phonepe":
            oid = random.randint(100,199)
            pid = random.randint(111111,999999)
            stud = Order.objects.all()

            for st in stud:
                orderfood = st.Order_Number
            order = Kitchen_Order(Order_Number = oid, items = orderfood, paymentid = pid, date = datetime.today())
            order.save()

            botvalue = f"Items : {orderfood} | Order Number : {oid} | Payment Id : {pid} | Your order will get ready soon!"

            return botvalue



        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    botvalue = f"{random.choice(intent['responses'])}"
        else:
            botvalue = f"I do not understand..."

        return botvalue
    


def orderchat(request):
    
    sentence = request.POST.get('input',False)
    sentence = sentence.replace("my order is", "")
    order_no = random.randint(100,200)
    views.orders(sentence,order_no)
    stud = Order.objects.all()

    for st in stud:
        orderfood = st.Order_Number
    botvalue = f"Please Confirm your order\n Items : {orderfood} Choose your payment option Gpay or phonepe"

    return botvalue