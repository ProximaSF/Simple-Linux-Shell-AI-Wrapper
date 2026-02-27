from botocore.exceptions import ClientError

def claude_Sonnet4_6(log_file_path, prompt, model_id, token_limit, client):
    with open(log_file_path, 'r', encoding='UTF-8') as f:
        f.seek(0)
        line = f.read()


        # Start a conversation with the user message.
        prompt = f"{prompt} \nFile content: {line}"
        conversation = [
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ]

        try:
            # Send the message to the model, using a basic inference configuration.
            response = client.converse(
                modelId=model_id,
                messages=conversation,
                inferenceConfig={"maxTokens": token_limit, "temperature": 0.5},
            )
            
            print("Running AI...")

            # Extract and print the response text.
            response_text = response["output"]["message"]["content"][0]["text"]
            return response_text

        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
            exit(1)


