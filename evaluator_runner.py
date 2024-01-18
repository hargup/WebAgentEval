import json
import subprocess
import sys
import tempfile
from datetime import datetime
import os
import argparse



def run_automator_task(automator_path, task_input, output_schema=None, auth_file=None):
    command = [automator_path, '-i', task_input]
    if output_schema:
        command += ['-o', output_schema]
    if auth_file:
        command += ['--auth', auth_file]

    result = subprocess.run(command, capture_output=True, text=True) 
    print(result) 
    return json.loads(result.stdout)

def compare_outputs(actual_output, expected_output):
    return actual_output == expected_output


def main():
    parser = argparse.ArgumentParser(description='Evaluator Runner')
    parser.add_argument('automator_path', help='Path to web automator')
    parser.add_argument('task_spec_file', help='Path to task specification file')
    parser.add_argument('--auth_file', help='Path to authentication file', default=None)
    args = parser.parse_args()

    automator_path = args.automator_path
    task_spec_file = args.task_spec_file
    auth_file = args.auth_file
    if auth_file and not os.path.isabs(auth_file):
        auth_file = os.path.abspath(auth_file)

    with open(task_spec_file, 'r') as file:
        tasks = json.load(file)

    report = {
        'total_tasks': len(tasks),
        'passed_tasks': 0,
        'failed_tasks': [],
    }

    for task in tasks:
        actual_output = run_automator_task(automator_path, task['input'], task.get('output_schema'), auth_file if task.get('auth') else None)
        if compare_outputs(actual_output, task['expected_output']):
            report['passed_tasks'] += 1
        else:
            report['failed_tasks'].append({
                'id': task['id'],
                'description': task['input'],
                'expected_output': task['expected_output'],
                'actual_output': actual_output
            })

    timestamp = datetime.now().isoformat()
    directory = 'reports'
    if not os.path.exists(directory):
        os.makedirs(directory)
    report_path = f'{directory}/{timestamp}.txt'
    with open(report_path, 'w') as file:
        file.write(json.dumps(report, indent=4))

    print(f"Total tasks: {report['total_tasks']}, Passed tasks: {report['passed_tasks']}, Failed tasks: {len(report['failed_tasks'])} \nFull report can be found at {report_path}")

if __name__ == "__main__":
    main()