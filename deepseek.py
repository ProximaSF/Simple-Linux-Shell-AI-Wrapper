import json
from botocore.exceptions import ClientError

def deepseek3_2(log_file_path, prompt, model_id, token_limit, client):
    with open(log_file_path, 'r', encoding='UTF-8') as f:
        f.seek(0)
        line = f.read()

        formatted_prompt = [{
            "role": "user",
            "content": f"{prompt} \nFile content: {line}"
        }]

        body = json.dumps({
            "messages": formatted_prompt,
            "max_tokens": token_limit,
            "temperature": 0.5,
            "top_p": 0.9,
        })
        try:
            print("Running AI...")
            # Invoke the model with the request.
            response = client.invoke_model(modelId=model_id, body=body)

            # Read the response body.
            model_response = json.loads(response["body"].read())

            # Extract choices.
            choices = model_response["choices"]

            # Print choices.
            #print(choices)
            
            response_text = choices[0]["message"]["content"]
            return response_text
        
        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
            exit(1)
