import os
from threading import Thread
from pyngrok import ngrok 

def run_streamlit():
	os.system('streamlit run ./webStreamLit.py --server.port 8509')
	
thread = Thread(target=run_streamlit)
thread.start()

# Add your ngrok token here
# ngrok.set_auth_token('2me69LDZkJwn0JmsxOHWNaAjaTr_4eFEK8EyXWRiRv22w3742')
ngrok.set_auth_token('2mhnHXdrDWQ19gC8vkdGDJjphDD_7QYRLgL2ggL9Whr6A5keW')

# Expose the app using ngrok
public_url = ngrok.connect(addr='8509', proto='http', bind_tls=True)
print(f'Your Streamlit app is live at: {public_url}')


# public_url = ngrok.connect(port='8501')
# print(f"Public URL: {public_url}")

