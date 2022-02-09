# Battlesnake Custom Attributes for New Relic

In this repository you can find code and instructions for instrumenting a Battlsnake's performance with [New Relic custom attributes](https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/collect-custom-attributes/). If you would like to add instrumentation in a language that is not yet documented in this repository, please use to following format for consistency (and consider submitting a PR!).

## Custom Attribute Format

Use the following JSON format for adding your custom attributes. These will appear alongside the relevant _Transaction_ data in New Relic.

This example uses the POST request from the [Battlesnake API docs](https://docs.battlesnake.com/references/api/sample-move-request):

```json
{
  "snakeGameId": "game-00fe20da-94ad-11ea-bb37",
  "snakeRules": "standard",
  "snakeTurn": 14,

  "snakeBoard": "base-64-encoded-JSON-object",

  "snakeName": "My Snake",
  "snakeId": "snake-508e96ac-94ad-11ea-bb37",
  "snakeHealth": 54,
  "snakeLength": 3,

  "snakeOpponent_1_Name": "Another Snake",
  "snakeOpponent_1_Id": "snake-b67f4906-94ae-11ea-bb37",
  "snakeOpponent_1_Health": 16,
  "snakeOpponent_1_Length": 4
}
```

_Note: due to the limit of custom attributes, this format only works for games with 7 snakes opponents (not including your own snake)._
