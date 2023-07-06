import argparse
import json

import gradio as gr
import requests


API_URL = "http://localhost:8000/generate"  # Replace with the actual API URL

def proxy_request(json_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(API_URL, json=json_data, headers=headers)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8001)
    parser.add_argument("--model-url",
                        type=str,
                        default="http://localhost:8000/generate")
    args = parser.parse_args()

    demo = gr.Interface(fn=proxy_request, inputs="json", outputs="json")
    demo.queue(concurrency_count=100).launch(server_name=args.host,
                                             server_port=args.port,
                                             share=True)