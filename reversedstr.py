class ReversedStr(str):
    def __new__(*args, **kwargs):
        string = str.__new__(*args, **kwargs)
        string = string[::-1]
        return string