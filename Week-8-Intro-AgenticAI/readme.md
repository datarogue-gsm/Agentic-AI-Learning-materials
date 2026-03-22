

# LangChain + OpenAI Quickstart: This demonstrates how to run a **basic LangChain + OpenAI** script using the `ChatOpenAI` model.



## Requirements: Before running the script, make sure you have:

* **Python 3.10+**
* An active **OpenAI API key**

---

## Installation: Create and activate a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies:


pip install langchain-openai python-dotenv

# or simply run:

pip install -r requirements.txt

---

## Set Up Environment Variables: Create a `.env` file in your project folder and add your OpenAI key(env_exampel added for reference):

```
OPENAI_API_KEY =  ""
OPENAI_API_BASE = ""

```

# Never commit .env file to GitHub.

