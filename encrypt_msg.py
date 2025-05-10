

def decrypt_msg(message: str) -> str:
    result = ''
    for i,chr in enumerate(message):
        if not chr.isdecimal():
            result += chr
        else:
            s = []
            idx = i + 2
            while c != ']' and len(s) == 0 
            
    return result




    
def main() -> None:
    """Ввод входных данных
    """
    # command_msg = input()
    print (get_first_digit_idx('a2[f]bc3[f]'))
    # print(decrypt_msg(command_msg))
    

if __name__ == '__main__':
    main()
