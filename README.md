# bmig5003_split_to_words
A command-line script that loads a file and splits &amp; filters it by word

# Install
```git clone https://github.com/zpeterg/bmig5003_split_to_words```

# Run
1. ```cd bmig5003_split_to_words```
2. ```python index.py -file=small_test.txt -start=foo -stop=bar -finish=enough```

You may also add new files at the root and change the -file, -start, -stop, -finish above. 

# Run Unit Tests
```python -m unittest discover -p '*test*.py'```