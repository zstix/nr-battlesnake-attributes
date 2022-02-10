import base64
import json

def encodeObject(obj: dict) -> str:
    """Turns an object into a base64 encoded JSON string for easier transport to
    New Relic.
    """
    return base64.urlsafe_b64encode(json.dumps(obj).encode()).decode()

def getSnakeData(snake: dict) -> str:
    """Gets some useful information about a snake and encodes it. This is necessary to
    keep the custom attribute size under 255bytes.
    """
    return encodeObject({
        "body": snake["body"],
        "head": snake["head"],
        "color": snake["customizations"]["color"]
    })

def getCustomAttributes(data: dict) -> dict:
    game = data["game"]
    board = data["board"]
    you = data["you"]

    attributes = {
        "snakeGameId": game["id"],
        "snakeRules": game["ruleset"]["name"],
        "snakeTurn": data["turn"],

        "snakeBoardHeight": board["height"],
        "snakeBoardWidth": board["width"],
        "snakeBoardFood": encodeObject(board["food"]),
        "snakeBoardHazards": encodeObject(board["hazards"]),

        "snakeName": you["name"],
        "snakeId": you["id"],
        "snakeHealth": you["health"],
        "snakeLength": you["length"],
        "snakeData": getSnakeData(you)
    }

    opponents = [s for s in board["snakes"] if s["id"] != you["id"]]

    for i, snake in enumerate(opponents):
        attributes["snakeOpponent_{}_Name".format(i + 1)] = snake["name"]
        attributes["snakeOpponent_{}_Id".format(i + 1)] = snake["id"]
        attributes["snakeOpponent_{}_Health".format(i + 1)] = snake["health"]
        attributes["snakeOpponent_{}_Length".format(i + 1)] = snake["length"]
        attributes["snakeOpponent_{}_Data".format(i + 1)] = getSnakeData(snake)

    return attributes

if __name__ == '__main__':
    input = {
      "game": {
        "id": "game-00fe20da-94ad-11ea-bb37",
        "ruleset": {
          "name": "standard",
          "version": "v.1.2.3"
        },
        "timeout": 500
      },
      "turn": 14,
      "board": {
        "height": 11,
        "width": 11,
        "food": [
          {"x": 5, "y": 5}, 
          {"x": 9, "y": 0}, 
          {"x": 2, "y": 6}
        ],
        "hazards": [
          {"x": 3, "y": 2}
        ],
        "snakes": [
          {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [
              {"x": 0, "y": 0}, 
              {"x": 1, "y": 0}, 
              {"x": 2, "y": 0}
            ],
            "latency": "111",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "",
            "customizations": {
                   "color":"#FF0000",
                   "head":"pixel",
                   "tail":"pixel"
                }
          }, 
          {
            "id": "snake-b67f4906-94ae-11ea-bb37",
            "name": "Another Snake",
            "health": 16,
            "body": [
              {"x": 5, "y": 4}, 
              {"x": 5, "y": 3}, 
              {"x": 6, "y": 3},
              {"x": 6, "y": 2}
            ],
            "latency": "222",
            "head": {"x": 5, "y": 4},
            "length": 4,
            "shout": "I'm not really sure...",
            "squad": "",
            "customizations":{
                   "color":"#26CF04",
                   "head":"silly",
                   "tail":"curled"
                }
          }
        ]
      },
      "you": {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": "",
        "customizations":{
                   "color":"#FF0000",
                   "head":"pixel",
                   "tail":"pixel"
                }
      }
    }
    result = getCustomAttributes(input)
    with open("result.json", "w") as write_file:
        json.dump(result, write_file, indent=2)
