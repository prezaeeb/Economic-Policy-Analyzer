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

<h3>Usage</h3>

1. **Download the file:** Save the provided code as economic_analyzer.py.

2. **Install dependencies:** Make sure you have the requests library installed.

3. **Run the script:** Execute the script from your terminal.
   
        -python economic_analyzer.py

The script will print the example policy and the resulting economic analysis provided by the LLM directly to your terminal. You can easily change the policy variable in the code to analyze different scenarios.
       
        
        ---- Economic Policy Analysis ---
            Policy: A new government policy is proposed to increase the minimum wage by 20% over the next two years.

            Analysis:
            The proposed 20% increase in the minimum wage could have mixed economic impacts. In terms of employment, it may lead to job losses in sectors with high labor costs, 
            as businesses might reduce staff to offset the higher wage expenses. However, it could also boost aggregate demand and GDP as low-income workers, who have a higher
            propensity to spend, see their purchasing power increase. Inflation could rise as businesses pass on higher labor costs to consumers. 
            The overall impact on market stability would depend on the scale of job losses versus the boost in consumer spending.

This project provides a clear example of how to integrate cutting-edge AI technology into economic analysis workflows, offering a fast way to get high-level insights into policy changes.

