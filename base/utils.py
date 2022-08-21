from typing import List


class Utils:
    @staticmethod
    def join_strings(str_list: List[str]) -> str:
        return ", ".join(str_list)

    @staticmethod
    def cat_str_end(line: str) -> str:
        elem = ''
        while elem != '(':
            line = line[:-1]
            elem = line[-1]
        return line[:-2]