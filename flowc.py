import translate, sys
import Errors
def bin(args:tuple[str, ...]) -> None:
    if len(args) != 4:
        raise Errors.ArgumentsError(f"Number of arguments is inavlid, expected 3 but recibed {len(args)-1} arguments")
    _, command, input1, input2 = args
    if command == "-c":
        with open(input1, "r") as f:
            code = f.read()
        code = translate.all(code)
        with open(input2, "w") as f:
            f.write(code)
        return None
    raise Errors.ArgumentsError(f"invalid command {command}")


if __name__ == "__main__":
    bin(tuple(sys.argv))