#!

# create a virtual environment
python -m venv venv

# install lark inside the virtual environment
source venv/bin/activate
python -m pip install lark

# make the script to run the project executable
chmod +x ./run.sh
export PATH="/workspaces/QuickSOAP:$PATH"
