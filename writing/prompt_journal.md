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

TODO: evaluation

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