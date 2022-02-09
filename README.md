# Battlesnake Custom Attributes for New Relic

In this repository you can find code and instructions for instrumenting a Battlsnake's performance with [New Relic custom attributes](https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/collect-custom-attributes/). If you would like to add instrumentation in a language that is not yet documented in this repository, please use to following format for consistency (and consider submitting a PR!).

## Custom Attribute Format

Use the following JSON format for adding your custom attributes. These will appear alongside the relevant _Transaction_ data in New Relic.

This example uses the POST request from the [Battlesnake API docs](https://docs.battlesnake.com/references/api/sample-move-request):

```json
{
  "battlesnakeGameId": "game-00fe20da-94ad-11ea-bb37",
  "battlesnakeRules": "standard",
  "battlesnakeTurn": 14,

  "battlesnakeBoard": "{\"height\":11,\"width\":11,\"food\":[{\"x\":5,\"y\":5},{\"x\":9,\"y\":0},{\"x\":2,\"y\":6}],\"hazards\":[{\"x\":3,\"y\":2}]",

  "battlesnakeName": "My Snake",
  "battlesnakeId": "snake-508e96ac-94ad-11ea-bb37",
  "battlesnakeHealth": 54,
  "battlesnakeLength": 3,
  "battlesnakeBody": "[{\"x\":0,\"y\":0},{\"x\":1,\"y\":0},{\"x\":2,\"y\":0}]",
  "battlesnakeHead": "{\"x\":0,\"y\":0}",
  "battlesnakeCustomizations": "{\"color\":\"#FF0000\",\"head\":\"pixel\",\"tail\":\"pixel\"}",

  "battlesnakeOpponent_1_Name": "My Snake",
  "battlesnakeOpponent_1_Id": "snake-508e96ac-94ad-11ea-bb37",
  "battlesnakeOpponent_1_Health": 54,
  "battlesnakeOpponent_1_Length": 3,
  "battlesnakeOpponent_1_Body": "[{\"x\":0,\"y\":0},{\"x\":1,\"y\":0},{\"x\":2,\"y\":0}]",
  "battlesnakeOpponent_1_Head": "{\"x\":0,\"y\":0}",
  "battlesnakeOpponent_1_Customizations": "{\"color\":\"#FF0000\",\"head\":\"pixel\",\"tail\":\"pixel\"}"
}
```

_Note: due to the limit of custom attributes, this format only works for games with 7 snakes opponents (not including your own snake)._
