export PYTHONPATH=.
PYTHONPATH=$PYTHONPATH:../src:../data
python -m unittest test_parser 
python -m unittest test_collector_unit 
python -m unittest test_collector 
