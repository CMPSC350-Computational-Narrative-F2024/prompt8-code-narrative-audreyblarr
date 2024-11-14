## 1. Prompts Used

- "Generate a series of Python-style functions that reflect teamwork and collaboration. Examples of collaboration may include functions that interact with one another or share data." (few-shot)
- "Generate a series of Python-style functions that reflect teamwork and collaboration. There should be three separate Python functions: the first two as individual functions and a third utilizing the first two functions in collaboration. After the three functions, there should be a use case of the above functions to demonstrate the collaboration." (chain of thought)
- "Generate a series of Python-style functions that reflect teamwork and collaboration. There should be three separate Python functions: the first two as individual functions and a third utilizing the first two functions in collaboration. After the three functions, there should be a use case of the above functions to demonstrate the collaboration. Ensure each function is present and includes enough specifics to serve as executable Python code." (chaining)

## 2. Prompting Strategy

I found a chaining strategy of prompting to be the most efficient in producing the output I desired. Few-shot prompting provided a good foundation for knowing what changes I'd implement to the code, while chain of thought was helpful in listing out the exact steps I desired the output to follow. Chaining did a great job of combining the second, chain of thought prompt with follow-up prompts to ensure the output included all the elements it was supposed to and served as executable code that I could implement to produce an output.

## 3. Output Evaluation

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

Firstly, the three prompts were crafted as I utilized Ollama's 'codegemma:2b' package to generate outputs. The first prompts, a simple few-shot approach, generated two functions that were very incomplete and ridden with random symbols that didn't serve any purpose. The functions didn't include any specified arguments, and only served to return 'print' statements and the value of 'data' incremented by 1. The purpose these functions would serve in terms of problem-solving remains very unclear. Next, the chain of thought prompting was intended to ensure the output followed very specified steps and included all the elements necessary to fulfill the narrative of collaboration. This output wasn't much different from the first, however, as it produced two functions titled 'first_function' and 'second_function' that each contained two arguments, and both functions were described to 'produce some operation' yet only returned the sum of the two arguments ('arg1' and 'arg2'). Then, there's a 'def' statement following the two functions signaling that there should be a third function, yet there wasn't a third function generated. This output was just as generic, unspecified, and incomplete as the first. While utilizing the third, chaining prompt, which included the second prompt with some further specifications, the generated output did show some improvement, but still not to the standards in which I desired. This output did include the two desired functions as well as a third use case function to tie the two functions together. However, the two functions only served to produce 'print' statements instead of including any sort of calculation or manipulation of data values, and the third function simply offered a way of printing both values at once. 

In order to efficiently compare the talents of Ollama's 'codegemma:2b' to Github's Copilot feature, I utilized the same three prompts for each LLM. Through even the first few-shot prompt I immediately noticed improvement with the generated output. The first output included four functions with specified arguments, and each function has its own purpose of manipulating the data provided in the arguments. Then, a complete use case was provided by establishing data types for the arguments, utilizing the functions with specific, real-world values to the arguments. The second output followed the desired structure I laid out in the chain of thought prompt, by including two functions, then a third function combining the two, and a use case to follow. This output didn't vary much from the first, other than generating one less function to better fit the structure I intended. The third output was the exact same as the second output, which means that the second prompt was so efficient in providing the generated output I intended, that the extra specifications I included in the third prompt were essentially useless.