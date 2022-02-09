import base64
import json

def getCustomAttributes(data: dict) -> dict:
    game = data["game"]
    board = data["board"]
    you = data["you"]

    attributes = {
        "snakeGameId": game["id"],
        "snakeRules": game["ruleset"]["name"],
        "snakeTurn": data["turn"],
        "snakeBoard": base64.urlsafe_b64encode(json.dumps(state).encode()),
        "snakeName": you["name"],
        "snakeId": you["id"],
        "snakeHealth": you["health"],
        "snakeLength": you["length"],
    }

    for i, snake in enumerate(board["snakes"]):
        if snake["id"] != you["id"]:
            attributes["snakeOpponent_{}_Name".format(i)] = snake["name"]
            attributes["snakeOpponent_{}_Id".format(i)] = snake["id"]
            attributes["snakeOpponent_{}_Health".format(i)] = snake["health"]
            attributes["snakeOpponent_{}_Length".format(i)] = snake["length"]

    return attributes
