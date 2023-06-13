import openai
import gradio as gr


# from decouple import config


# openai.api_key = OpenAI_Key = config("OpenAI_Key")

openai.api_key = "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"

messages = [
    {
        "role":"system",
        "content" : "This is a chatbot that only answer questions related to Vivien Chua. For questions not related to Vivien Chua, reply with Sorry, I do not know."
		},
    {
        "role":"user",
        "content":"Who is Vivien Chua?"
    },
    {
        "role":"assistant",
        "content":"Vivien Chua is Chief Investment Officer and co-founder at Meadowfield Capital. Her professional experience includes private equity, data analytics, and risk management. Vivien started her career as an Assistant Professor at the National University of Singapore, after returning from a Singapore National Research Foundation Ph.D. scholarship. Vivien graduated with a Ph.D. and M.S. in Engineering from Stanford University, and a B.S. in Engineering from Georgia Institute of Technology. She was awarded MIT Technology Review Innovators Under 35 Asia Pacific, SG 100 Women In Tech and Insurance Business Elite Women."
    }
]


def generate_response(input):
    if input:
        messages.append({
            "role":"user",
            "content":input
				})
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages
				)
        reply = chat.choices[0].message.content
        messages.append({
            "role":"assistant",
            "content":reply
				})
        return reply

def my_chatbot(input, history):
    history = history or []
    my_history = list(sum(history, ()))
    my_history.append(input)
    my_input = ' '.join(my_history)
    output = generate_response(my_input)
    history.append((input, output))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("""<h1><center>My Chatbot</center></h1>""")
    chatbot = gr.Chatbot()
    state = gr.State()
    text = gr.Textbox(placeholder="Hello. Ask me a question.")
    submit = gr.Button("SEND")
    submit.click(my_chatbot, inputs=[text, state], outputs=[chatbot, state])

demo.launch(share = True)
    
