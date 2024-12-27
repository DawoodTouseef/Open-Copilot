try:
    from ...utils.db import load_nexusai_url,load_nexusai_api_key
except ImportError:
    from core.utils.db import load_nexusai_url,load_nexusai_api_key
import requests

def stt_nexusai(audio_file,file):
    # Set the headers
    token=load_nexusai_api_key()
    base_url=load_nexusai_url()
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}',

    }
    # Build the URL
    import os
    file_name = os.path.basename(file)
    url = f"{str(base_url).rstrip('/')}/audio/api/v1/transcriptions"
    files = {
        'file': (file_name, audio_file, 'audio/wav'),  # Provide filename and content type
    }
    # Send the POST request to the API
    response = requests.post(url, headers=headers, files=files)

    # Check for errors in the response
    if response.status_code != 200:
        error = response.json().get('detail', 'An error occurred')
        return f"Error: {error}"

    return response.json()['text']

if __name__=="__main__":
    with open('E:\\jarvis\\Client\\JARVIS2\\core\\utils\\artifacts\\mic_record.wav','rb' ) as f:
        print(stt_nexusai(f,'E:\\jarvis\\Client\\JARVIS2\\core\\utils\\artifacts\\mic_record.wav'))