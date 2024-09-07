class Input:
    def __init__(self, message: str = None, type: any = any, nullable: bool = False):
        from colorama import Fore, Back, Style

        self.val = None
        self.message = Fore.BLUE + message + Fore.LIGHTWHITE_EX
        self.nullable = nullable

        if not message:
            return input()

        res = input(self.message)

        if type is bool:
            yes_str = set(["y", "yes"])
            no_str = set(["n", "no"])
            self.get_bool(res, yes_str, no_str)

        if type is str:
            self.get_str(res)

        if type is int:
            self.get_int(res)

    def get_bool(self, res: any, yes_str: set, no_str: set):
        if res.lower() in yes_str or len(res) == 0:
            self.val = True
        elif res.lower() in no_str:
            self.val = False
        elif self.nullable and len(res) == 0:
            self.val = True
        else:
            res = input(self.message)
            self.get_bool(res, yes_str, no_str)

    def get_str(self, res: str):
        if len(res) == 0 and self.nullable:
            return None

        if len(res) == 0:  # if user just hit enter
            res = len(res)

        try:
            _ = int(res)
            res = input(self.message)
            self.get_str(res)
        except ValueError:
            self.val = res

    def get_int(self, res: str):
        if len(res) == 0 and self.nullable:
            self.val = None
        if len(res) == 0:
            res = " "
        try:
            res = int(res)
            self.val = res
        except ValueError:
            res = input(self.message)
            self.get_int(res)


if __name__ == "__main__":
    try:
        i = Input(message="test", type=bool, nullable=False)
        print(i.val)
    except KeyboardInterrupt:
        exit(0)
