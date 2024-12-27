try:
    from ...utils.db import load_nexusai_url,load_nexusai_api_key
except ImportError:
    from core.utils.db import load_nexusai_url, load_nexusai_api_key
import requests


def tts_nexusai(text_chunk, location):
    url=load_nexusai_url()
    api_key=load_nexusai_api_key()
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    # Build the URL
    url = f"{str(url).rstrip('/')}/audio/api/v1/speech"
    params={
        "input":text_chunk,
        "voice":'ftvI5ig770iLKJP3eaTT'
    }
    response = requests.post(url,json=params, headers=headers)
    # Save the streaming content to a file

    with open(location, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


