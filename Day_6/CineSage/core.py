from dotenv import load_dotenv  # Loads environment variables from a .env file.
from langchain_core.prompts import ChatPromptTemplate  # Builds structured prompts for chat models.
from pydantic import BaseModel  # Base class for defining structured data models.
from typing import List, Optional  # Type hints for lists and optional values.
from langchain_core.output_parsers import PydanticOutputParser  # Parses model output into a Pydantic model.

load_dotenv()  # Reads .env and sets environment variables for API keys, etc.
from langchain_mistralai import ChatMistralAI  # Chat model client for Mistral.


model = ChatMistralAI(model='mistral-small-2506')  # Initializes the chat model with a specific model name.



class Movie(BaseModel):  # Defines the structure of the movie data we want.
    title: str  # Movie title (required).
    release_year: Optional[int]  # Release year (optional integer).
    genre: List[str]  # One or more genres (list of strings).
    director: Optional[str]  # Director name (optional string).
    cast: List[str]  # Main cast names (list of strings).
    rating: Optional[float]  # Rating score (optional float).
    summary: str  # Short summary of the movie (required).



parser = PydanticOutputParser(pydantic_object=Movie)  # Creates a parser that outputs a Movie object.


prompt = ChatPromptTemplate.from_messages([  # Builds a chat prompt from multiple message roles.
    (
        'system',  # System message sets overall task for the model.
        """
Extract movie information from the paragraph
     {format_instructions}
""",  # Instruction text with a placeholder for formatting rules.
    ),
    ("human", "{paragraph}"),  # Human message provides the actual input paragraph.
])  # End of prompt message list.



para = input("Give your paragraph : ")  # Takes a paragraph as input from the user.

final_prompt = prompt.invoke(  # Fills the prompt template with actual values.
    {
        "paragraph": para,  # Inserts the user's paragraph into the prompt.
        'format_instructions': parser.get_format_instructions(),  # Adds JSON format instructions.
    }
)  # End of prompt invocation.

response = model.invoke(final_prompt)  # Sends the prompt to the model and gets a response.
movie_data = parser.parse(response.content)  # Parses the model's text into a Movie object.

print(movie_data)  # Prints the structured movie data to the console.
