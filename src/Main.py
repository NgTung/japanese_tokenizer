import os
import sys

from ArgumentParser import ArgumentParser
from CSV import CSV
from JapaneseTokenizer import MeCabTokenizer


def tokenizing(csv_import_path, csv_export_path):
    csv_obj = CSV(csv_import_path)
    csv_data = csv_obj.get_data()

    sentence_arr = []
    for row in csv_data:
        for cell in row:
            sentence_arr.append(cell)

    tokenizer = MeCabTokenizer(tagger='-Ochasen')
    output_arr = []
    stop_words = ['。', '、', '･']
    for sentence in sentence_arr:
        tokens = tokenizer.parse_to_node(sentence)
        surface = []
        while tokens:
            if tokens.surface and tokens.surface not in stop_words:
                surface.append(tokens.surface)
            tokens = tokens.next
        if len(surface) > 0:
            output_arr.append([sentence, " ".join(surface)])

    csv_obj.export(csv_export_path, output_arr)


if __name__ == "__main__":
    usage_cmd = 'Usage: \n'
    usage_cmd += ' ' + os.path.basename(__file__)
    usage_cmd += ' -i <input_file> -e <export_file>'

    raw_input = ArgumentParser(sys.argv[1:], usage_cmd)

    if not raw_input.validate():
        raw_input.print_usage()
        exit(2)

    # Parse & get argument value
    args = raw_input.parse(["i", "e"], ["import=", "export="])
    tokenizing(raw_input.get_value_by_key("-i", args), raw_input.get_value_by_key("-e", args))
