import requests
import json
from dotenv import load_dotenv
import os
import time

# Load the .env file
dotenv = load_dotenv()


# def make_prompt(user_message, objects, player, water_tiles, water_drops):
#     # Create a prompt
#     print(f"User message: {user_message}")
#     # print(f"Objects: {objects}")
#     fruits_string = ""
#     for position, fruit in objects.items():
#         print(f"Fruit:{fruit.type} with position:{position} and water:{fruit.water}")
#         fruits_string += f"({position}, Fruit: {fruit.type} - water: {fruit.water})\n"
#     print(f"Player: {player}")
#     print(f"Water tiles: {water_tiles}")
#     print("Water drops: ", {water_drops})
#     prompt = f"""
#     You are a farmer assisstant in charge of picking, dropping and growing fruits at various places in a 15x15 map.
#     Fruits have 3 stages of growth: small (water = 0), mid (water = 1) and big (water = 2) as fully grown. One water drop makes a fruit grow by one stage.
#     Those are some tips for the game:
#     1/ The map is composed of cells on an orthogonal grid. Each cell can be occupied only by one agent, target or obstacle.
#     2/ The bottom left corner of the map is the position (0,0). The x-axis is horizontal and the y-axis is vertical.

#     Each fruit will be given through a row with 3 elements: Position, Fruit type and water level. For example, (Position: (2, 8), Fruit: Banana - water: 0) means that there is an banana at position (2, 8) with 0 water so it is petite.
#     The fruits are located at the following positions:
#     {fruits_string}
#     The player is located at the following x and y positions:
#     {player}
#     The water tiles are located at the following positions:
#     {water_tiles}
#     The player has {water_drops} water drops.

#     You have access to three ACTIONS: "PICK", "DROP", "MOVE x,y" and "DROP_WATER".
#     1/ "PICK": Pick up an object at the current position and stacks it on the player's inventory.
#     2/ "DROP": Drop the last object in the stack created by the PICK action at the current position and removes it from the inventory.
#     3/ "MOVE x,y": Move the player to a new position on the map. The new position is defined by the x and y coordinates.
#     4/ "DROP_WATER" : Drop water at the current position. The player has a limited number of water drops (max 3). Dropping water makes a fruit grow by one stage. You can only drop water on a fruit which is on the ground.
#     5/ Player can have water drops when just passing on water tiles but it is not required to do another action to get water drops.
#     6/ It is IMPOSSIBLE to place multiple objects at the same place. You can't drop an object where one is already placed. You con't drop an object on water tiles


#     Here is the user's message:
#     {user_message}


#     By using the functions given, create algorithms that will do what the user wants.
#     Use the functions in a creative way to achieve the desired result.
#     Do not forget to use the functions in the correct order to achieve the desired result.
#     Only answer with the required actions and thoughts in the following format:

#     RESPONSE FORMAT:
#     THOUGHTS: Based on the information I listed above, in 50 words, do reasoning about what the next task should be.
#     COMMAND: The next COMMAND. A COMMAND can be composed of one or multiple actions, which are defined above. You can do as many actions as you want in a COMMAND, in any order. Split every action by a single ";" and no space.
#     """
#     return prompt


def make_prompt(user_message, objects, player, water_tiles, water_drops):
    # Create a prompt
    print(f"User message: {user_message}")
    fruits_string = ""
    for position, fruit in objects.items():
        print(f"Fruit:{fruit.type} with position:{position} and water:{fruit.water}")
        fruits_string += f"({position}, Fruit: {fruit.type} - water: {fruit.water})\n"
    print(f"Player: {player}")
    print(f"Water tiles: {water_tiles}")
    print("Water drops: ", {water_drops})
    prompt = f"""
    You are a farmer assistant in charge of picking, dropping, and growing fruits at various places in a 15x15 map.
    Fruits have 3 stages of growth: small (water = 0), mid (water = 1), and big (water = 2) as fully grown. One water drop makes a fruit grow by one stage.

    Map Description:
    1. The map is a 15x15 orthogonal grid where each cell can hold only one agent, target, or obstacle.
    2. The bottom left corner of the map is (0,0). The x-axis is horizontal, and the y-axis is vertical.

    Fruit Details:
    Each fruit will be described with Position, Fruit type, and Water level. Example:
    - (Position: (2, 8), Fruit: Banana - water: 0)
    
    Current Game State:
    The fruits are located at the following positions:
    {fruits_string}
    The player is located at the following position:
    {player}
    The water tiles are located at the following positions:
    {water_tiles}
    The player has {water_drops} water drops.

    Available Actions:
    - PICK: Pick up an object at the current position and stack it in the player's inventory.
    - DROP: Drop the last picked object from the stack at the current position.
    - MOVE x,y: Move the player to the specified position.
    - DROP_WATER: Use one water drop on the current position to make a fruit grow by one stage.

    Additional Rules:
    - Before moving to water fruits, make sure to have enough water drops for all the fruits to water.
    - Water drops can be refilled by passing over water tiles. Player gets 1 water drop per water tile. But you can pass over the same water tile multiple times.
    - You can have a maximum of 3 water drops.
    - A fruit can only grow if water is dropped directly on it while on the ground.
    - You cannot drop a fruit on a water tile or a cell that already contains an object.

    Examples of Actions:
    - To move to position (3,5), pick an apple, drop it, and water it:
      COMMAND: MOVE 3,5;PICK;DROP;DROP_WATER
    - To grow a fruit already on the map:
      COMMAND: MOVE 2,3;DROP_WATER

    Response Format:
    THOUGHTS: Based on the current game state and user message, describe the plan in around 50 words.
    COMMAND: Provide a sequence of actions separated by a semicolon.

    ### User's Message:
    {user_message}

    Generate the optimal COMMAND sequence following the rules above. Decomposes the instruction into several logical sub-instructions.
    """
    return prompt


# Function to extract the thoughts and command from the text
def extract_thoughts_and_command(text):
    # Initialiser les variables pour stocker les thoughts et la commande
    thoughts = None
    action = None

    # Extraire les thoughts
    if "THOUGHTS:" in text:
        start_thoughts = text.index("THOUGHTS:") + len("THOUGHTS:")
        end_thoughts = text.index("COMMAND:")
        thoughts = text[start_thoughts:end_thoughts].strip()

    # Extraire la commande
    if "COMMAND:" in text:
        command_part = text.split("COMMAND:")[1].strip()
        action = command_part

    return thoughts, action


# Function to make a request to the API
def make_request(prompt):
    def send_request():
        # Make a request to the API
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('API_KEY')}",
            },
            data=json.dumps(
                {
                    "model": "deepseek/deepseek-chat",  # Optional
                    "messages": [{"role": "user", "content": prompt}],
                }
            ),
        )
        return response.json()

    # Send request
    response = send_request()
    # print(response)

    # Check if the rate limit was reached
    while "error" in response and response["error"]["code"] == 429:
        # Wait for 30 seconds and try again
        print("Rate limit reached, waiting for 30 seconds")
        time.sleep(30)
        response = send_request()

    # Check if the request was successful
    if "error" in response:
        raise Exception(f"Failed to make the request: {response}")

    # Get the answer from the response
    answer = response["choices"][0]["message"]["content"]
    return answer
