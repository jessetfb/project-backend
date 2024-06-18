import sys
import os

# Add the parent directory of the current file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modals.properties import Property

my_property = Property()  # Use Property somewhere in your code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) # type: ignore