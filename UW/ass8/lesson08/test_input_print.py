import input_print


def test_input_print():
    input_values = [2, 3]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    def mock_print(s):
        output.append(s)

    input_print.input = mock_input
    input_print.print = mock_print

    input_print.main()

    assert output == [
        "First: ",
        "Second: ",
        "The result is 5",
    ]
