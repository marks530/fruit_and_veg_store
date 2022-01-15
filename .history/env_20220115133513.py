import os
if os.path.exists("env.py"):
  import env 
  
os.environ["DEVELOPMENT"] = "False"   