import requests
import json
import os

def ollama_request(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "codegemma:2b",
        "prompt": prompt,
        "max_tokens": 500
    }
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data, stream=True)
        full_response = ""

        # Iterate through the stream, decoding each chunk separately
        for chunk in response.iter_lines():
            if chunk:  # If the chunk is not empty
                try:
                    # Decode the JSON chunk
                    decoded_chunk = json.loads(chunk)
                    
                    # Check if 'response' key exists in decoded_chunk
                    if 'response' in decoded_chunk:
                        full_response += decoded_chunk['response']  # Append the response part
                    else:
                        print("Warning: 'response' key not found in chunk:", decoded_chunk)
                except json.JSONDecodeError:
                    print("Error decoding chunk:", chunk)

        # Return the full response after the entire response is processed
        return full_response if full_response else None

    except requests.exceptions.RequestException as e:
        print(f"Error querying the library: {e}")
        return None


def main():
    prompt = "Generate a series of Python-style functions that reflect teamwork and collaboration. There should be three separate Python functions: the first two as individual functions and a third utilizing the first two functions in collaboration. After the three functions, there should be a use case of the above functions to demonstrate the collaboration. Ensurre each function is present and includes enough specifics to serve as executable Python code."
    ollama_output = ollama_request(prompt)
    print(ollama_output)

if __name__ == "__main__":
    main()
