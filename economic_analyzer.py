#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This script uses an LLM to analyze the potential economic impact of a policy.
# It requires the 'requests' library to interact with the LLM API.
# You can install it using pip:
# pip install requests

import requests
import json

def analyze_economic_policy(policy_text):
    """
    Sends a policy description to an LLM for economic analysis.

    Args:
        policy_text (str): The text description of the economic policy.

    Returns:
        str: The LLM's analysis of the policy's economic impact,
             or an error message if the request fails.
    """
    # Define your API key (leave as an empty string)
    api_key = ""
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

    # Define the system instruction to act as an economic analyst.
    # The instruction guides the LLM to provide a specific type of analysis.
    system_instruction = {
        "parts": [{
            "text": "You are a professional economic analyst. Your task is to provide a concise, single-paragraph summary of the potential economic impacts of the provided policy. Focus on key indicators such as GDP, inflation, employment, and market stability. State your analysis clearly and avoid jargon."
        }]
    }

    # Construct the user query with the policy text.
    user_query = f"Analyze the economic impact of the following policy:\n\n{policy_text}"

    # Construct the payload for the API request.
    payload = {
        "contents": [{
            "parts": [{
                "text": user_query
            }]
        }],
        # Using Google Search grounding to ensure the analysis is based on
        # up-to-date and relevant economic principles and data.
        "tools": [{
            "google_search": {}
        }],
        "systemInstruction": system_instruction,
        "generationConfig": {
            # No specific mime type is needed here, as we want free-form text.
            "responseMimeType": "text/plain"
        }
    }

    print("Sending policy to LLM for analysis...")
    
    try:
        # Make the API call with a timeout.
        response = requests.post(api_url, json=payload, timeout=30)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        result = response.json()
        
        # Extract the generated text from the response.
        analysis = result['candidates'][0]['content']['parts'][0]['text']
        
        return analysis

    except requests.exceptions.RequestException as e:
        return f"An error occurred during the API call: {e}"
    except (KeyError, IndexError) as e:
        return f"Could not parse API response. Malformed response or missing data: {e}"

if __name__ == "__main__":
    # Example policy to analyze.
    policy = "A new government policy is proposed to increase the minimum wage by 20% over the next two years."
    
    # Get the economic analysis from the LLM.
    economic_analysis = analyze_economic_policy(policy)
    
    print("\n--- Economic Policy Analysis ---")
    print(f"Policy: {policy}")
    print("\nAnalysis:")
    print(economic_analysis)

