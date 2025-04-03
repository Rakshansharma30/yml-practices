import yaml
import json
from collections import defaultdict

# Load YAML data
with open('employees.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Basic access to data
print(f"Number of employees: {len(data['employees'])}")
print(f"First employee: {data['employees'][0]['name']}")

# Process and transform the data
def analyze_employee_data(employees_data):
    # Create summary statistics
    stats = {
        'total_employees': len(employees_data),
        'avg_age': sum(emp['age'] for emp in employees_data) / len(employees_data),
        'positions': set(emp['position'] for emp in employees_data),
        'skills_count': defaultdict(int)
    }
    
    # Count skills across all employees
    for emp in employees_data:
        for skill in emp['skills']:
            stats['skills_count'][skill] += 1
    
    # Convert to regular dict for easier serialization
    stats['skills_count'] = dict(stats['skills_count'])
    stats['positions'] = list(stats['positions'])
    
    return stats

# Get stats and project mapping
stats = analyze_employee_data(data['employees'])
print("\nEmployee Statistics:")
print(json.dumps(stats, indent=2))

# Create project to employee mapping
project_mapping = defaultdict(list)
for emp in data['employees']:
    for project in emp['projects']:
        project_mapping[project['name']].append({
            'name': emp['name'],
            'role': project['role']
        })

print("\nProject Team Composition:")
for project, team in project_mapping.items():
    print(f"\n{project}:")
    for member in team:
        print(f"  - {member['name']} ({member['role']})")

# Export processed data to JSON
processed_data = {
    'statistics': stats,
    'project_teams': dict(project_mapping)
}

with open('processed_employee_data.json', 'w') as f:
    json.dump(processed_data, f, indent=2)

print("\nProcessed data exported to 'processed_employee_data.json'")