# Product Ingredient Analyzer

This Streamlit application is designed to analyze images of product packaging, particularly the ingredient lists, and extract information about their contents using a combination of AI and web searching.

## Overview

The application leverages the following technologies:

*   **Streamlit:** For building the interactive web application.
*   **Phi-AI:** As the underlying agent framework.
*   **Google Gemini API:** To analyze the images of ingredient lists using a multi-modal model.
*   **Tavily API:** To perform web searches and retrieve additional information, when needed.

This tool can be used to quickly understand the ingredients of various products by simply uploading a picture or using an example image.

## Features

*   **Image Upload:** Allows users to upload images of product packaging for analysis.
*   **Camera Input:** Users can also take a live photo of the product packaging.
*   **Example Products:** Includes a few example products for users to try without needing to upload their own images.
*   **Detailed Analysis:** Leverages a large language model to provide a detailed breakdown of the product based on the image provided.
*   **Web Searching:** Uses the Tavily API to perform web searches to enhance analysis.
*   **Interactive UI:** Built with Streamlit, offering a simple and intuitive user interface.
* **Clear Error Handling:** Provides user friendly error messages in case the program encounters an issue or if the API keys are not set.

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

*   **Python 3.7+:**
*   **pip:** Python's package manager
*   **Git:** (Optional for cloning from GitHub)

### Installation

1.  **Clone the repository (if applicable):**

    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [YOUR_PROJECT_DIRECTORY]
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    ```

    *   **Activate it:**
        *   **On Windows:**

            ```bash
            .venv\Scripts\activate
            ```
        *   **On macOS and Linux:**

            ```bash
            source .venv/bin/activate
            ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file lists all required libraries. Make sure this file is created first (see instructions below).

4.  **Set up API keys:**
    *   Get your API keys from [Tavily](https://tavily.com/) and [Google AI](https://ai.google.dev/).
    *   Create a `.env` file in your project's root directory.
    * Add the following lines to your `.env` file and replace placeholders with your actual keys:
        ```env
        TAVILY_API=[YOUR_TAVILY_API_KEY]
        GEMINI_API=[YOUR_GOOGLE_GEMINI_API_KEY]
        ```
    *Ensure that `.env` is in your `.gitignore`.

### Running the application

To start the Streamlit app, navigate to your project directory and run:

```bash
streamlit run app.py
```

Open the URL provided in your browser (usually `http://localhost:8501`).

## Usage

1.  **Select Tab:** Choose between "Example Products," "Upload Image," and "Take Photo".
2.  **Select Image:** If on the Example products tab, select one of the examples. If using "Upload Image" or "Take Photo," upload or capture an image of the product's packaging.
3.  **Analyze:** Click on the "Analyze" button to start the analysis.
4.  **View Results:** The analysis result will appear below the image.

## Project Structure

```
├── app.py                # Main Streamlit application file
├── constants.py          # Contains system prompts and instructions
├── images/              # Folder for example images
│    ├── ...
├── .env                  # File to hold API keys (DO NOT commit this to git)
├── .gitignore            # File that lists ignored files
├── README.md             # This file
└── requirements.txt      # List of Python dependencies
```

## Creating requirements.txt
You should create `requirements.txt` by running:
```
pip freeze > requirements.txt
```

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.