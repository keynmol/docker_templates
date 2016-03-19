import argparse
import re
import os


def combinations(options):
    if len(options) == 0:
        return []

    opt = options[0]
    results = []
    if len(options) > 1:
        for value in opt[1]:
            ahead = combinations(options[1:len(options)])
            results += [([(opt[0], value)] + x) for x in ahead]
    else:
        results = [[(opt[0], value)] for value in opt[1]]

    return results


def print_file(source, template_values, output):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    def format_line(l):
        return re.sub("<<(" + "|".join(template_values.keys()) + ")>>", "{\\1}", l).format(**template_values)

    with open(source, "r") as inp:
        with open(output, "w") as outp:
            for raw_line in inp:
                outp.write(format_line(raw_line))

parser = argparse.ArgumentParser("generate.py")
parser.add_argument("--label-template", type=str, required=True)
parser.add_argument("--files", nargs='*')
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--base-folder", default=".")
parser.add_argument("--output-folder", default=None)

args, unknown = parser.parse_known_args()

if not args.output_folder:
    args.output_folder = args.base_folder

all_params = re.findall("([A-Z_]+)", args.label_template)
new_parser = argparse.ArgumentParser()

for p in all_params:
    new_parser.add_argument("--" + p, nargs='*')

values = list(new_parser.parse_args(unknown).__dict__.items())

files = ["Dockerfile"] + args.files


def pj(*args):
    return os.path.join(*args)

for c in combinations(values):
    label_hash = dict(c)
    new_label = re.sub("(" + "|".join(label_hash.keys()) + ")", "{\\1}", args.label_template)
    new_label = new_label.format(**label_hash)

    for f in files:
        print_file(pj(args.base_folder, f), label_hash, pj(args.output_folder, new_label, f))

    print("docker build -t {name}:{label} {path}".format(name=args.name, label=new_label, path=pj(args.output_folder, new_label)))
