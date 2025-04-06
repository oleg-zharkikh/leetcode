# номер успешной посылки:
# 1
def decrypt_mesage(encrypted_msg: str) -> str:
    result = ''

    multplicator_idx = get_digit_idx(encrypted_msg)
    if multplicator == -1:
        return encrypted_msg
    else:
        multplicator_value = int(encrypted_msg[multplicator_idx])
        end_block
        return encrypted_msg


    return result



def main() -> None:
    """Ввод входных данных,
    3[a]2[bc]
    aaabcbc

    Команда: 2[в3[ш]]с Расшифровка: «вшшшвшшшс»
    """
    encrypted_command_line = input()

    decrypted_command_line = decrypt_mesage(encrypted_command_line)
    print(decrypted_command_line)


if __name__ == '__main__':
    main()
