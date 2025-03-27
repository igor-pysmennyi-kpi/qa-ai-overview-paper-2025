import os

BASE_PROMPT = """
You work as a QA engineer. Generate concise test cases in the following format:

1. Test case ID and title  
2. Test data – data required to execute a test case. For example, login and password or customer age to fill in UI form to trigger some specific expected validation message. 
3. Preconditions – initial state of the system required to execute test case  
4. Steps – an ordered action sequence the tester must perform to execute a test scenario. This executable sequence is called test scenario.  
5. Expected results – expected system state and behavior after performing test steps.  
6. Postconditions – optional set of steps required to revert system to blank state.  
   
!!!Important test steps should cover only focal scenario and not preconditions  
For following User-Story: 

"""
class StoryPrompt:
    def __init__(self, name, content, output_dir):
        self.name = name
        self.content = content
        self.output_dir = output_dir
        
def read_prompts(stories_folder):
    story_prompts = []
    
    for filename in os.listdir(stories_folder):
        file_path = os.path.join(stories_folder, filename)
        
        # Ensure it's a file (not a directory)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            promt_name = filename.rsplit( ".", 1 )[ 0 ]
            story_prompt = StoryPrompt(
                name=promt_name,  
                content=content,  
                output_dir=f"tc/generated/{promt_name}"
            )
            story_prompts.append(story_prompt)
    
    return story_prompts

if __name__ == "__main__":
    story_prompts = read_prompts("stories")
    
    # Print details of each StoryPrompt object
    for prompt in story_prompts:
        print(prompt.name)
        print(prompt.content)
        print(prompt.output_dir)
        print("-" * 50)