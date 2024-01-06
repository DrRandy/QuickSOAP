#!

cd /workspaces/QuickSOAP/sandbox

python -m codegen2
python -m createtests

cd /workspaces/QuickSOAP/quick

python -m unittest discover
