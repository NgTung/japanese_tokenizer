## Japanese Tokenizer Tool

This is a simple python script for tokenizing Japanese. The output looks like below:

```これは本です``` ~> ```これ は 本 です```

### Prepare:

- Python3
- Mecab
- Pandas

### Run:

Commands:
```bash
$ python src/Main.py -i <input_file> -e <export_file>
```
Ex:
```bash
$ python src/Main.py -i example_input/input.csv -e output.csv
```