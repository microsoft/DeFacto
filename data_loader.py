import json


def load_all_data():
    data = {}
    with open("./data/test.jsonl") as f:
        test_data = [json.loads(line) for line in f]
    data["test"] = test_data
    with open("./data/train.jsonl") as f:
        train_data = [json.loads(line) for line in f]
    data["train"] = train_data
    with open("./data/val.jsonl") as f:
        val_data = [json.loads(line) for line in f]
    data["val"] = val_data
    print("Loaded data")
    print("Train size: ", len(train_data))
    print("Val size: ", len(val_data))
    print("Test size: ", len(test_data))
    print("example: ", json.dumps(train_data[1], indent=2))
    return data

if __name__ == "__main__":
    data = load_all_data()
    