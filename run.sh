#!

cd /workspaces/QuickSOAP/codegen

python -m generate_code
python -m generate_tests

cp ../test/test_generatedtests.py ../quick

cd /workspaces/QuickSOAP/quick

python -m unittest discover

rm test_generatedtests.py
