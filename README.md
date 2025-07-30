# 🧠 Text2UI Generator

Unleash Your UI Ideas with AI-Powered HTML Generation

This project presents a powerful Text-to-UI Generator built with Streamlit and leveraging advanced Large Language Models (LLMs) to transform natural language descriptions into complete, modern, and responsive HTML web pages with Tailwind CSS. Perfect for rapid prototyping, design exploration, and demonstrating the power of AI in web development.

---

## ✨ Features

- **Natural Language to UI:** Describe your desired UI in plain English, and the AI generates the corresponding HTML code.
- **Tailwind CSS Integration:** All generated UIs are styled using Tailwind CSS utility classes for a clean, modern, and responsive design.
- **Complete & Production-Ready Code:** The AI generates a single, self-contained HTML file, ready to be viewed in any web browser.
- **Responsive Design:** Generated UIs are inherently responsive, adapting gracefully to various screen sizes (mobile, tablet, desktop).
- **Interactive Components:** Includes basic JavaScript for common UI interactions like fade-in animations on scroll, smooth navigation, and functional elements (e.g., tabs, modals).
- **Side-by-Side View:** Streamlit UI provides an intuitive interface with a code editor and a live preview side-by-side.
- **Full-Screen Preview Toggle:** Easily switch to a full-screen preview of the generated UI for a better visual experience.
- **Secure API Key Handling:** Utilizes environment variables for secure management of API keys.

---

## 🚀 How It Works

The core of this application is the `ui_generator.py` module, which interacts with a powerful Large Language Model (LLM) via the OpenRouter API.

1. **User Prompt:** You provide a detailed text description of the UI you want to generate.
   - _Example:_  
     `"Generate a modern landing page for a mobile phone store with a hero section, featured products, and a footer."`

2. **Prompt Engineering:** A carefully crafted "system prompt" (acting as a "Senior Frontend Engineer" persona) guides the LLM to generate high-quality, Tailwind CSS-based HTML. This prompt includes strict requirements for structure, styling, responsiveness, and interactivity.

3. **LLM Generation:** The LLM processes your prompt and the system instructions, generating the complete HTML, including all necessary Tailwind CSS classes and JavaScript.

4. **Streamlit Display:** The generated HTML code is displayed in a text editor, and a live preview is rendered directly within the Streamlit application.

---

## 🛠️ Technologies Used

- **Python 3.x:** The primary programming language.
- **Streamlit:** For building the interactive web application UI.
- **openai Python Library:** To interact with the OpenRouter API.
- **python-dotenv:** For loading environment variables from a .env file.
- **OpenRouter API:** A unified API gateway providing access to various LLMs.
- **DeepSeek R1 Free Model:** The primary LLM used for UI generation.
- **Tailwind CSS:** A utility-first CSS framework for rapid and responsive UI styling.
- **Font Awesome:** For scalable vector icons.

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.8+ installed
- Git installed

### 1. Clone the Repository

```sh
git clone https://github.com/mzu-2410z/Text2UI/
cd Text2UI
```

### 2. Set up a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# Or for Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```
If you don't have `requirements.txt` yet, you can create it after installing the individual packages:

```sh
pip install streamlit openai python-dotenv pyngrok
pip freeze > requirements.txt
```

### 4. Configure API Key (Crucial!)

Your application needs an API key to communicate with the OpenRouter LLM.

- Get your OpenRouter API Key:
  - Go to [OpenRouter.ai](https://openrouter.ai/) and sign up for a free account.
  - Generate a new API key in your dashboard.
- Create a `.env` file in the project root:

```
OPENROUTER_API_KEY="sk-or-v1-YOUR_OPENROUTER_API_KEY_HERE"
```

- Add `.env` to `.gitignore`:

```
# Environment variables
.env
```

## ▶️ Running the Application

### Method 1: Local

```sh
streamlit run app.py
```

- Opens at: `http://localhost:8501`

## 📝 Usage Guide

1. **Open the Application:** Use your local or public ngrok URL.
2. **Enter Your Prompt:** In the text area, describe the UI you want the AI to generate. Be as detailed and specific as possible.
3. **Generate UI:** Click the "Generate UI" button. Wait for the spinner while the AI works.
4. **View Results:**  
    - See the complete HTML in the left panel.
    - Live preview in the right panel.
    - Toggle full screen with the "Toggle Full Screen Preview" button.

### Example Prompts

- "Generate a modern, dark-themed dashboard for a data analytics platform with a sidebar navigation, a main content area showing a sales chart, and a user profile card."
- "Create a responsive e-commerce product listing page with at least 5 product cards, each having an image, title, price, and an 'Add to Cart' button. Use a vibrant color scheme."
- "Design a minimalist contact us page for a photography studio, including a contact form, map placeholder, and social media links."

---

## 💡 Tips for Effective Prompting

- **Be Specific:** Instead of "a form," try "a login form with email, password, and 'Forgot Password' link."
- **Define Layout:** Use terms like "two columns," "grid layout," "sidebar," "full-width hero."
- **Specify Components:** Explicitly ask for "navigation bar," "feature cards," "testimonials section," "pricing table," "modal," "dropdown menu," etc.
- **Describe Aesthetics:** Use adjectives like "modern," "minimalist," "vibrant," "dark-themed," "professional," "elegant." Mention color preferences (e.g., "blue and white palette," "earthy tones").
- **Request Interactivity:** If you want specific JavaScript, mention it (e.g., "with a carousel," "with tab switching," "with form validation").
- **Provide Content Details:** For lists or cards, suggest the number of items (e.g., "at least 3 feature cards," "5 product listings").

---

## 🔮 Future Improvements

- Advanced Interactivity: More complex JavaScript components (e.g., interactive charts, drag-and-drop interfaces).
- Component Library Integration: Option to use libraries like Shadcn UI, Material UI.
- Multi-Page Generation: Generate multi-page websites with linked navigation.
- Code Export Options: Download buttons for the generated HTML.
- User Authentication: Save and manage generated UIs with user accounts.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙏 Acknowledgements

- Inspired by the capabilities of Text-to-UI models like DeepSite.
- Powered by OpenRouter.ai and the DeepSeek R1 LLM.
- Built with Streamlit and Tailwind CSS.
#
