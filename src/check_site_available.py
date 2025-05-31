from concurrent.futures import ThreadPoolExecutor

import requests
import streamlit as st


def check_site_availabale(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36)'}
        response = requests.get(url , headers=headers)
        if response.status_code == 200:
           return True
        return False
    except Exception as e:
        return False

# --- Streamlit UI ---
st.title("🔍 Website Availability Checker")

urls_input = st.text_area("Enter URLs (one per line):")

if st.button("Check Availability"):
    urls = [url.strip() for url in urls_input.strip().splitlines() if url.strip()] # make a lit of urls from text_area
    if urls:
        with ThreadPoolExecutor() as executor:
            futures = executor.map(check_site_availabale, urls)
      
        st.subheader("Results")
        for url, is_up in zip(urls, futures):
            status = "✅ Available" if is_up else "❌ Not Available"
            st.markdown(f"- **{url}** — {status}")
    else:
        st.warning("Please enter at least one URL.")
