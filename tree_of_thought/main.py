# This is a Tree of Thoughts demo
#That needs an API key to work
# so you must have a valid API key from OpenAi (ChatGPT)
# And pip install tree-of-thoughts-llm
# It will cost about $1.50 to run
# And might take several minutes
# It is cheaper with 'gpt-3.5'
# Check out more Tree of Life at 
# https://github.com/princeton-nlp/tree-of-thought-llm/tree/master/tree_of_life
import argparse
from tot.methods.bfs import solve
from tot.tasks.game24 import Game24Task

args = argparse.Namespace(backend='gpt-4', 
                          temperature=0.7, t
                          ask='game24', 
                          naive_run=False, 
                          prompt_sample=None, 
                          method_generate='propose', 
                          method_evaluate='value', 
                          method_select='greedy', 
                          n_generate_sample=1, 
                          n_evaluate_sample=3, 
                          n_select_sample=5)

task = Game24Task()
ys, infos = solve(args, task, 900)
print(ys[0])