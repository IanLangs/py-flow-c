import translate, sys
import Errors
def bin(args:tuple[str]=sys.argv) -> None:
    if len(args) != 4:
        raise Errors.ArgumentsError(f"Number of arguments is inavlid, expected 3 but recibed {len(args)-1} arguments")
    command: str = args[1]
    inputs:tuple[str] = args[2:]
    if command == "-c":
        with open(inputs[0], "r") as f:
            code = f.read()
        code = translate.all(code)
        with open(inputs[1], "w") as f:
            f.write(code)
        return None
    raise Errors.ArgumentsError(f"invalid command {command}")


if __name__ == "__main__":
    bin()