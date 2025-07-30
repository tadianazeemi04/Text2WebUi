# %%writefile ui_generator.py
import os
import openai
import streamlit as st
from dotenv import load_dotenv # Import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()

# --- OpenRouter API Configuration ---
# The API key is now loaded from the environment variable OPENROUTER_API_KEY
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Configure the OpenAI client to use the OpenRouter API endpoint
client = openai.OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# Basic check to ensure the API key is loaded
if not OPENROUTER_API_KEY:
    st.error("OpenRouter API key not found. Please set the OPENROUTER_API_KEY environment variable or in your .env file.")
    st.stop() # Stop the Streamlit app if the key is missing

# Configure the OpenAI client to use the OpenRouter API endpoint
client = openai.OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# --- UI Generation Function ---
def generate_ui(prompt):
    """
    Generates a complete HTML page with Tailwind CSS based on a user prompt
    using the Meta Llama 3.1 405B Instruct model from OpenRouter.
    """
    try:
        response = client.chat.completions.create(
            
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Senior Frontend Engineer specializing in cutting-edge web design. "
                        "Your task is to generate a single, *visually stunning*, *highly interactive*, "
                        "and *production-ready* HTML page. Your code MUST use **Tailwind CSS** for all styling. "
                        "The entire response MUST be the complete code for a single file, with all styling handled "
                        "by Tailwind utility classes. Do NOT write any CSS in a `<style>` tag.\n\n"
                        
                        "Strict Requirements for Excellence:\n"
                        "1.  **Overall Aesthetic**: Create a cohesive and modern design that feels premium and engaging. "
                        "Utilize harmonious color palettes, subtle gradients, and sophisticated `box-shadow` effects for depth. "
                        "Ensure consistent typography and spacing throughout the page. Think about a unique 'brand identity' "
                        "for the given prompt and reflect it in the design choices.\n"
                        "2.  **Tailwind Integration**: Always include the Tailwind CSS CDN link in the `<head>` section: "
                        "`<script src='https://cdn.tailwindcss.com'></script>`. "
                        "3.  **HTML Structure & Content**: Use modern HTML5 semantic tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, etc.). "
                        "Generate *meaningful mock content* (e.g., detailed product descriptions, realistic testimonials, "
                        "specific service benefits) that fits the theme, instead of generic placeholders. "
                        "The page should feel complete and ready to present.\n"
                        "4.  **Tailwind Classes Only**: All styling, including layout, colors, typography, and responsiveness, must be applied "
                        "directly to HTML elements using Tailwind CSS utility classes (e.g., `flex`, `bg-blue-500`, `text-lg`, `shadow-xl`, `hover:scale-105`).\n"
                        "5.  **Flawless Responsiveness**: Implement a mobile-first approach. Use Tailwind's responsive prefixes (`sm:`, `md:`, `lg:`) "
                        "extensively to ensure the design adapts gracefully to all screen sizes. For mobile views, "
                        "the navigation should collapse into a functional hamburger menu, and content should reflow into a single column.\n"
                        "6.  **Dynamic & Interactive Components**: Design and style common UI components with advanced touches:\n"
                        "    * **Hero Section**: Prominent, engaging headline, compelling tagline, and a highly styled Call-to-Action (CTA) button with a noticeable hover effect.\n"
                        "    * **Feature/Product Blocks**: Visually distinct cards with subtle animations (e.g., `hover:scale-105`, `transition-all`). Use appropriate icons (Font Awesome) or relevant emojis for visual appeal.\n"
                        "    * **Forms**: If a form is included, ensure it's well-structured with clear labels, input fields, and a submit button. Add basic client-side validation or success/error message display via JavaScript if applicable.\n"
                        "    * **Navigation**: Implement smooth scrolling for internal links.\n"
                        "7.  **External Assets**: If the design requires icons, always include the Font Awesome CDN link in the `<head>` section. The link for Font Awesome is `<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'>`.\n"
                        "8.  **JavaScript Interactivity**: Always include a well-commented JavaScript snippet for a 'fade-in on scroll' effect for sections/elements to enhance the user experience. If the prompt implies other interactivity (e.g., a dropdown menu, image carousel, tab switching), generate the necessary JavaScript within a `<script>` tag at the end of the `<body>`.\n"
                        "9.  **Code Quality & Readability**: Ensure the generated HTML is clean, well-indented, and easy to read. Use comments within the `<script>` tag to explain JavaScript logic. The overall code should reflect best practices for maintainability.\n"
                        "10. **Output Integrity**: The final output must be a single, complete HTML document. Do not truncate the code. Do not add any text or explanations outside of the document structure. Your ENTIRE response MUST be the code, and nothing else. Begin your response with `<!DOCTYPE html>`."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=8192,
            timeout=60.0
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        # This block will catch specific API errors from OpenRouter
        st.error(f"OpenRouter API Error: {e.status_code} - {e.response}")
        return None
    except Exception as e:
        # This block catches other unexpected errors
        st.error(f"An unexpected error occurred: {e}")
        return None