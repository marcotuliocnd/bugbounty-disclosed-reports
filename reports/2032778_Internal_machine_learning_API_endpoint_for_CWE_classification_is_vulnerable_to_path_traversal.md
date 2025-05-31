# Internal machine learning API endpoint for CWE classification is vulnerable to path traversal

## Report Details
- **Report ID**: 2032778
- **URL**: https://hackerone.com/reports/2032778
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-20T22:02:06.309Z
- **Disclosed**: 2023-07-05T15:05:25.578Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
HackerOne has an internal machine learning API that exposes inference endpoints for numerous machine learning / artificial intelligence solutions. In one of the endpoints, `/predict/report_weakness_id`, which is used to classify report input, a path traversal vulnerability exists that could lead to remote code execution.

# Proof of concept
The `request.version` and `request.trained_at` parameters are both vulnerable to path traversal. To reproduce, run any of the following curl commands inside the local Docker container:

**trained_at**
```
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

**version**
```
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

The vulnerable code is shown below. The `version` and `trained_at` inputs are interpolated directly into the path, as can be seen on line 29. The `AutoTokenizer.from_pretrained` function is then called to load the tokenizer into memory.

```python
@app.post(
    "/predict/report_weakness_id",
    summary="An endpoint to suggest report's weakness id.",
)
async def report_weakness_id(request: ReportWeaknessIdModelRequest):
    """
    To try the endpoint in the Swagger UI, click on **Try it out** and copy-paste the below example in the request body box
    ```
    {
        "version":"v1",
        "trained_at": "2023-01-01T00_00_00Z",
        "input": [
            {
                "title": "test xss",
                "num_of_top_predictions": 3
            }
        ]
    }
    ```
    """
    input = request.input[0]
    title = preprocess_text(input.title)

    top_n = int(
        input.num_of_top_predictions or 3
    )  # as a start, it's by default set as 3

    model_dirpath = pathlib.Path(
        f"{os.path.dirname(__file__)}/../models/report_weakness_id/{request.version}/{request.trained_at}/"
    )

    tokenizer = AutoTokenizer.from_pretrained(model_dirpath, use_fast=True)
```

## Impact

An attacker would be able to execute arbitrary python code if they were able to get a joblib file onto the ML API (i.e. as a temporary file).

## Attachments
No attachments
