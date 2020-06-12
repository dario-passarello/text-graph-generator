import render
import analyzer
import argparse
import os


def get_raw_text(filename: str):
    with open(filename, "r") as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description='Creates Text Graph, from a text file')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    text = get_raw_text(args.filename)
    graph_struct = analyzer.get_graph_struct_from_text("output", text)
    render.render_graph(render.build_graph(graph_struct), out_filename="out/%s_out" % (os.path.basename(args.filename)))


if __name__ == "__main__":
    main()
