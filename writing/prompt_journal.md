## 1. Prompts Used

Try at least three variations and use the same final prompts for both Copilot and another LLM

- "Generate a series of Python-style functions that reflect teamwork and collaboration. Examples of collaboration may include functions that interact with one another or share data." (few-shot)
- "Generate a series of Python-style functions that reflect teamwork and collaboration. There should be three separate Python functions: the first two as individual functions and a third utilizing the first two functions in collaboration. After the three functions, there should be a use case of the above functions to demonstrate the collaboration." (chain of thought)
- "Generate a series of Python-style functions that reflect teamwork and collaboration. There should be three separate Python functions: the first two as individual functions and a third utilizing the first two functions in collaboration. After the three functions, there should be a use case of the above functions to demonstrate the collaboration. Ensure each function is present and includes enough specifics to serve as executable Python code." (chaining)

## 2. Prompting Strategy

TODO: What was your strategy with prompting. What worked and what didn't work? Did you employ a specific prompting technique (zero-, few-, many-shot, chaining, chain of thought, meta prompting)?

## 3. Output Evaluation

For each generated code output, consider:
    - Narrative Structure: How does the organization reflect the theme? Is there a clear flow that resembles a narrative?
    - Commentary and Documentation: How do Copilot’s comments contribute to the narrative? Do they add meaning to the code?
    - Design Choices: Evaluate how Copilot's naming conventions, variable usage, and logic choices enhance or detract from the narrative.

### Copilot

Output 1:
```python
# Function to add a team member
def add_team_member(team, member):
    team.append(member)
    return team

# Function to assign a task to a team member
def assign_task(team, tasks, member, task):
    if member in team:
        tasks[member] = task
    else:
        print(f"Member {member} is not in the team.")
    return tasks

# Function to get the task assigned to a team member
def get_task(tasks, member):
    return tasks.get(member, "No task assigned")

# Function to display all team members and their tasks
def display_team_tasks(team, tasks):
    for member in team:
        task = get_task(tasks, member)
        print(f"{member}: {task}")

# Example usage
team = []
tasks = {}

# Adding team members
team = add_team_member(team, "Alice")
team = add_team_member(team, "Bob")

# Assigning tasks
tasks = assign_task(team, tasks, "Alice", "Develop feature X")
tasks = assign_task(team, tasks, "Bob", "Test feature Y")

# Displaying team tasks
display_team_tasks(team, tasks)
```

Output 2:
```python
# Function to add a team member
def add_team_member(team, member):
    team.append(member)
    return team

# Function to assign a task to a team member
def assign_task(tasks, member, task):
    tasks[member] = task
    return tasks

# Function to manage team and tasks
def manage_team_and_tasks(team, tasks, member, task):
    team = add_team_member(team, member)
    tasks = assign_task(tasks, member, task)
    return team, tasks

# Example usage
team = []
tasks = {}

# Adding and assigning tasks to team members
team, tasks = manage_team_and_tasks(team, tasks, "Alice", "Develop feature X")
team, tasks = manage_team_and_tasks(team, tasks, "Bob", "Test feature Y")

# Displaying team tasks
for member in team:
    print(f"{member}: {tasks[member]}")
```

Output 3:
```python
# Function to add a team member
def add_team_member(team, member):
    if member not in team:
        team.append(member)
    return team

# Function to assign a task to a team member
def assign_task(tasks, member, task):
    tasks[member] = task
    return tasks

# Function to manage team and tasks
def manage_team_and_tasks(team, tasks, member, task):
    team = add_team_member(team, member)
    tasks = assign_task(tasks, member, task)
    return team, tasks

# Example usage
team = []
tasks = {}

# Adding and assigning tasks to team members
team, tasks = manage_team_and_tasks(team, tasks, "Alice", "Develop feature X")
team, tasks = manage_team_and_tasks(team, tasks, "Bob", "Test feature Y")

# Displaying team tasks
for member in team:
    print(f"{member}: {tasks[member]}")
```

### Other Single LLM: Ollama's codegemma:2b

Output 1:
```json
 35 points.ipynb
# %%
def team_work(func):
    def wrapper(*args, **kwargs):
        print("Team members are working on the same function")
        return func(*args, **kwargs)
    return wrapper

@team_work
def process_data(data):
    print("Processing data")
    return data + 1

result = process_data(10)
print(result)

# %%
```

Output 2:
```json
(Use any language you want).
 def first_function(arg1, arg2):
     """
     This function will be used for team work and collaboration
     """
     # Perform some operation
     result = arg1 + arg2
     return result

 def second_function(arg1, arg2):
     """
     This function will be used for team work and collaboration
     """
     # Perform some operation
     result = arg1 + arg2
     return result
 def
 ```

 Output 3:
 ```json
 def team_member(name):
    """
    Prints a greeting for a team member.

    Args:
        name (str): The name of the team member.
    """
    print(f"Hello, {name}!")

def team_leader(name):
    """
    Prints a greeting for a team leader.

    Args:
        name (str): The name of the team leader.
    """
    print(f"Congratulations, {name}!")

def team_collaboration(name):
    """
    Prints a greeting for a team member and team leader.

    Args:
        name (str): The name of the team member.
    """
    team_member(name)
    team_leader(name)
```

## 4. Reflection

TODO: How did your prompt iterations impacted the narrative quality of the generated code? How did Copilot's suggestions supported or hindered the story within the code? 