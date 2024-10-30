def process_elements(input_lst):
    while True:
        assert len(input_lst) > 1:
        for element in input_lst:
            if isinstance(element, (str, int)):
                if element.lower() != "stop":
                    try:
                        got_number = int(element)
                    except ValueError:
                        got_number = False
                    else:
                        if got_number > 0:
                            print("Got a positive number!")
                        elif got_number == 0:
                            print("Got zero.")
                        else:
                            print("Got a negative number.")
                else:
                    print("Found stop command:", element)

        break

# Use this function
input_lst = ["1", "-2", "3", "stop"]
process_elements(input_lst)
