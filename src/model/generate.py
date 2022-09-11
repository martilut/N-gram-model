import argparse
import pickle


def generate_text(model_path, prefix, length, seed):
    with open(model_path, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    result = loaded_model.generate(length, seed, prefix)
    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, help="Path to trained model")
    parser.add_argument("--prefix", type=str, default=None, help="Prefix: word sequence separated with spaces")
    parser.add_argument("--length", type=int, help="Text size to generate")
    parser.add_argument("--seed", type=int, default=None, help="Seed to initialize generator")

    args = parser.parse_args()
    generate_text(args.model, args.prefix, args.length, args.seed)
