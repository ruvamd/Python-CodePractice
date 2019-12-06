from dotenv import load_dotenv
import os
load_dotenv()
os_version=os.getenv('OS')
print(os_version)
