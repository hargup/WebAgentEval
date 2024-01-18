## Usage

This script is used to run the evaluator for the web automator. It requires the path to the web automator, the task specification file, and optionally, an authentication file.

Parameters:
- `/path/to/web_automator`: This is the path to the web automator that you want to evaluate.
- `/path/to/task_spec_file.json`: This is the path to the JSON file that contains the task specifications.
- `--auth_file /path/to/auth_file.json`: (Optional) This is the path to the JSON file that contains the authentication information. If not provided, the script will run without authentication.

```
python evaluator_runner.py /path/to/web_automator /path/to/task_spec_file.json [--auth_file /path/to/auth_file.json]
```


## Test Spec File


[NOTE: The spec will probably change and move from a static json file to some dynamic python/js test]
[Our current test spec file is present at eval/task_spec.json]
The test file spec is a JSON file that contains a list of tasks for the web automator to perform. Each task is represented as an object with the following properties:

- `id`: A unique identifier for the task.
- `input`: A string that describes the task to be performed. This could be a URL to visit, a form to fill, or a data to retrieve.
- `expected_output`: An object that describes the expected output of the task. This is used to evaluate the performance of the web automator.
- `output_schema`: This is currently not used and is set to null.
- `auth`: A boolean value that indicates whether the task requires authentication. If true, the web automator will use the authentication information provided in the auth_file.

Here is an example of a task in the test file spec:

```
{
    "id": "data_retrieval_weather",
    "input": "Extract the current temperature and weather condition from Weather.com for New York City. URL: https://weather.com/weather/today/l/f892433d7660da170347398eb8e3d722d8d362fe7dd15af16ce88324e1b96e70",
    "expected_output": {
        "temperature_fahrenheit": "48",
        "condition": "cloudy"
    },
    "output_schema": null,
    "auth": false
}
```

In this example, the web automator is expected to visit the provided URL, extract the current temperature and weather condition for New York City, and return an object with the temperature in Fahrenheit and the weather condition.
