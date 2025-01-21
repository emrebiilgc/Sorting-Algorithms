import sys

def bubble_sort(myList, output_file):
    n = len(myList)

    already_sorted = True
    for i in range(n - 1):
        if myList[i] > myList[i + 1]:
            already_sorted = False
            break

    if n == 0 or n == 1 or already_sorted:
        print("Already sorted!")
    else:
        pass_number = 0
        swaps_made = False

        while True:
            for j in range(0, n - 1):
                if myList[j] > myList[j + 1]:
                    myList[j], myList[j + 1] = myList[j + 1], myList[j]
                    swaps_made = True

            pass_number += 1

            with open(output_file[0], 'a') as f:
                line = "Pass {}: {}".format(pass_number, " ".join(str(x) for x in myList))
                f.write(line.rstrip() + ("\n" if swaps_made else ""))

            if not swaps_made:
                break

            swaps_made = False

def insertion_sort(myList, output_file):
    is_sorted = True
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        print("Already sorted!")
        return

    with open(output_file[1], 'a') as output:
        for i in range(1, len(myList)):
            key = myList[i]
            j = i - 1
            while j >= 0 and key < myList[j]:
                myList[j + 1] = myList[j]
                j -= 1

            myList[j + 1] = key

            # Concatenate elements into a string with spaces
            state_string = "Pass {}: {}".format(i, " ".join(str(x) for x in myList))

            # Write the state string to the output file
            output.write(state_string)

            if i < len(myList) - 1:  # Add newline if it's not the last pass
                output.write("\n")

            if all(myList[k] <= myList[k + 1] for k in range(len(myList) - 1)):
                break

def main():
    if len(sys.argv) not in [2, 4]:
        print("Usage: python script.py input_file [bubble_output_file insertion_output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    bubble_output_file = sys.argv[2] if len(sys.argv) == 4 else "bubble_output.txt"
    insertion_output_file = sys.argv[3] if len(sys.argv) == 4 else "insertion_output.txt"

    try:
        with open(input_file, 'r') as f:
            my_sorted_list = [int(x) for x in f.readline().split()]
    except FileNotFoundError:
        print("Input file not found.")
        sys.exit(1)

    # Perform bubble sort
    bubble_sort(my_sorted_list.copy(), [bubble_output_file, insertion_output_file])

    # Perform insertion sort
    insertion_sort(my_sorted_list.copy(), [bubble_output_file, insertion_output_file])

if __name__ == "__main__":
    main()
