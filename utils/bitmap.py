from typing import List, Optional


class Bitmap:
    __matrix: List[List[int]]
    __class_name: Optional[str]

    def __init__(self, matrix: List[List[int]], class_name: Optional[str] = None):
        self.__matrix = matrix
        self.__class_name = class_name

    def set_class_name(self, class_name: str) -> None:
        self.__class_name = class_name

    def get_class_name(self) -> Optional[str]:
        return self.__class_name

    def get_matrix(self) -> List[List[int]]:
        return self.__matrix

    def __str__(self):
        return f"class= {self.__class_name}, matrix= {self.__matrix}"

    def __repr__(self):
        return f"class= {self.__class_name}, matrix= {self.__matrix}"
