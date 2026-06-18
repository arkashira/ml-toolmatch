import argparse
import json
from dataclasses import dataclass

@dataclass
class Tool:
    name: str
    description: str

def load_configuration(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def recommend_tools(configuration, input_data):
    tools = configuration['tools']
    recommended_tools = []
    for tool in tools:
        if tool['required_input'] in input_data:
            recommended_tools.append(Tool(tool['name'], tool['description']))
    return recommended_tools

def main():
    parser = argparse.ArgumentParser(description='ML Toolmatch')
    parser.add_argument('--config', help='Path to configuration file', required=True)
    parser.add_argument('--input', help='Path to input data file', required=True)
    args = parser.parse_args()

    configuration = load_configuration(args.config)
    input_data = load_configuration(args.input)

    recommended_tools = recommend_tools(configuration, input_data)

    print('Recommended tools:')
    for tool in recommended_tools:
        print(f'{tool.name}: {tool.description}')

if __name__ == '__main__':
    main()
