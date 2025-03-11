from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyCEDSZcXkmKYv3JY--y2GvDXnpi1X-61pw")  # Replace with your actual API key

def get_recipe(dish_name):
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")  # Use your correct model
        prompt = f"Provide a structured recipe for {dish_name} with the following format:\n\n" \
                 "Ingredients:\n- List all ingredients needed.\n\n" \
                 "Steps:\n1. Step-by-step instructions to prepare the dish."
        response = model.generate_content(prompt)

        return response.text if response else "Sorry, I couldn't generate a recipe."
    except Exception as e:
        return f"Error: {str(e)}"



@app.route('/', methods=['GET', 'POST'])
def home():
    recipe = ""
    if request.method == 'POST':
        dish = request.form.get('dish', '').lower()
        recipe = get_recipe(dish)
    return render_template('index.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
