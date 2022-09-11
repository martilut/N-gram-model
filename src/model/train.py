import os
import argparse
import pickle

from NgramModel import NgramModel
from src.utils.text_parsing import parse_text


def train_model(input_dir, model_path, prefix_len):
    model = NgramModel(prefix_len)
    files = os.listdir(input_dir)
    words = []
    for file in files:
        file_path = os.path.join(input_dir, file)
        with open(file_path, 'r') as f:
            raw_text = f.read()
            words += parse_text(raw_text)
    model.fit(words)
    with open(os.path.join(model_path, 'model.pkl'), 'wb') as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, help="Path to dir with text files")
    parser.add_argument("--model", type=str, help="Path to save trained model")
    parser.add_argument("--prefix_length", type=int, default=2, help="Prefix size for N-gram model")

    args = parser.parse_args()
    train_model(args.input_dir, args.model, args.prefix_length)
