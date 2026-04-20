import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EX_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../output.txt")
EX_OUTPUT2_PATH = os.path.join(SCRIPT_DIR, "../temp_test_file/expected_output2.txt")

def read_testcases(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Split on blank lines
    testcases = content.split("\n\n")

    # Normalize each testcase (remove trailing spaces, etc.)
    testcases = [
        "\n".join(line.strip() for line in tc.strip().split("\n"))
        for tc in testcases
    ]

    return testcases


expected = read_testcases(EX_OUTPUT_PATH)
output = read_testcases(EX_OUTPUT2_PATH)

# Compare
for i, (exp, out) in enumerate(zip(expected, output), 1):
    if exp != out:
        print(f"\033[91m Testcase {i} failed\033[0m")
        print(expected)
        print(output)
    else:
        print(f"\033[92m Testcase {i} passed\033[0m")

# Extra safety checks
if len(expected) != len(output):
    print("⚠️ Number of testcases mismatch!")
    print(expected)
    print(output)
    print(len(expected),len(output))



