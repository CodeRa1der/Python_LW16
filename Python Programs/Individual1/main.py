#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module

if __name__ == "__main__":
    input_data = input("Введите значения через пробел: ").split()
    input_numbers = [int(x) for x in input_data]
    max_func = module.outer_function()
    print("Максимальное значение:", max(input_numbers))
    min_func = module.outer_function(type='min')
    print("Минимальное значение:", min(input_numbers))
    