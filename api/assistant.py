from openai import OpenAI


def product_query(product_details, user_question, api_key):
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Ask Cafa providing information about products."},
                {"role": "user", "content": f"Product details: {product_details}\n\nUser question: {user_question}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


