import yaml
from pprint import pprint

class MealPlanner():
    def __init__(self, yaml_file):
        self.yaml_read = self.reader(yaml_file)

    def reader(self, yaml_file):
        with open(yaml_file, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

if __name__ == '__main__':
    yaml_file = 'framework.yaml'
    planner = MealPlanner(yaml_file)
    pprint(planner.yaml_read)
