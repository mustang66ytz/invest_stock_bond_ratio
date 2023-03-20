import csv

def load_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # skip the first row
        next(reader)
        # extract current from the second row
        first_row = next(reader)
        current = int(first_row[2])
        # extract history from the remaining rows
        history = [int(row[2]) for row in reader]
    return current, history

def get_current_index(current, history, horizon):
    history.insert(0, current)
    history = history[:horizon]
    history = sorted(history)
    print(history)
    ratio = float(history.index(current)+1) / float(len(history))
    return ratio

def main():
    current, history = load_csv_file('dummy_test.csv')
    horizon = 4
    current_index = get_current_index(current, history, horizon)
    print("Current index:", current_index)

if __name__ == "__main__":
    main()
