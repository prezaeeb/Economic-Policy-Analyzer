# Economic-Policy-Analyzer
This Python script is designed to demonstrate how a Large Language Model (LLM) can be used to analyze and summarize complex economic policies. 
It acts as a tool for a quick, professional-level economic impact assessment by leveraging the power of a generative AI.

The script connects to the Gemini API to analyze a given policy and provide a concise summary of its potential effects on key economic indicators such as GDP, inflation, and employment.

<h3>Prerequisites</h3>
To run this script, you will need the requests library. You can install it using pip:

    -pip install requests

<h3>How It Works</h3>
The script operates on a simple principle:

1. **Policy Input:** A user-defined economic policy is provided as a text string.

2. **LLM Analysis:** The script sends this policy text to a powerful LLM, along with a system_instruction that directs the model to act as a professional economic analyst. This ensures the output is focused and relevant.

3. **Grounded Response:** The API call is configured to use Google Search grounding, which helps the LLM provide an analysis based on real-world economic principles and data. This makes the output more informed and accurate.

4. **Summary Generation:** The LLM's response is a concise, single-paragraph summary of the policy's potential impacts on key economic indicators.

