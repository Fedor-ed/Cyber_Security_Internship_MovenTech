import boto3
import time

# Initialize AWS Lambda client
lambda_client = boto3.client('lambda')

# Function to invoke a Lambda function and collect performance metrics


def invoke_lambda_function(function_name):
    start_time = time.time()
    response = lambda_client.invoke(FunctionName=function_name)
    end_time = time.time()

    execution_time = end_time - start_time
    memory_used = response['MemoryUsed']
    # Other relevant metrics can be collected similarly

    return {
        'execution_time': execution_time,
        'memory_used': memory_used
        # Add other metrics here
    }

# Function to analyze collected metrics and detect anomalies


def detect_anomalies(metrics):
    # Example: Simple anomaly detection based on execution time threshold
    for metric in metrics:
        if metric['execution_time'] > 10:  # Example threshold: 10 seconds
            print(
                f"Anomaly detected: Execution time exceeded threshold for function {metric['function_name']}")
        # Add more sophisticated anomaly detection logic here

# Main function to orchestrate the monitoring process


def main():
    # List of Lambda functions to monitor
    functions_to_monitor = ['function1', 'function2', 'function3']

    while True:
        collected_metrics = []
        for function_name in functions_to_monitor:
            metrics = invoke_lambda_function(function_name)
            metrics['function_name'] = function_name
            collected_metrics.append(metrics)

        detect_anomalies(collected_metrics)

        # Sleep for a certain interval before collecting metrics again
        time.sleep(60)  # Example: Collect metrics every minute


if __name__ == "__main__":
    main()
