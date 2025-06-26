custom_css = """
<style>
    /* App Background */
    .stApp {
        background-color: lightgrey !important;
    }

    .main, .block-container {
        background-color: lightgrey !important;
        padding: 1rem 2rem;
    }

    /* Global Font */
    body {
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title Style */
    h1 {
        color: green;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }

    /* Text Area */
    .stTextArea textarea {
        background-color: mintcream;
        color: black;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.5rem;
        border: 2px solid green;
    }

    /* Button Styling */
    .stButton button {
        background-color: seagreen;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        border: none;
        box-shadow: 1px 1px 4px grey;
    }

    .stButton button:hover {
        background-color: darkgreen;
        transition: 0.3s ease-in-out;
    }

    /* Info / Warning / GPT Output Boxes */
    .stAlert, .stSuccess, .stInfo, .stError {
        font-size: 16px;
        font-weight: 500;
        background-color: white !important;
        color: black !important;
        border: 2px solid green;
        border-radius: 10px;
        padding: 1rem;
        margin-top: 1rem;
    }

    /* Emotion Result Text */
    .emotion-result {
        font-weight: bold;
        font-size: 18px;
        color: darkgreen;
    }
</style>
"""
