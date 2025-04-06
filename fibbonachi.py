def get_fibbonachi(v):
    if v == 0 or v == 1: 
        return 1
    else:
        return get_fibbonachi(v-1) + get_fibbonachi(v-2)



def main() -> None:
    version = int(input())

    number_of_calc = get_fibbonachi(version)
    print(number_of_calc)


if __name__ == '__main__':
    main()
