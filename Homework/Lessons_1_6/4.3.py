def palindrome(word):
    # lowercase the string
    lc_word = word.lower()
    # define the loop range divided by 2 since we will compare chars from the beginning and end at once
    loop_range = range(len(lc_word) // 2)

    for i in loop_range:
        # compare chars from beginning and end
        if lc_word[0] == lc_word[-1]:
            # remove the first and last chars if they are equal
            lc_word = lc_word.removeprefix(lc_word[0]).removesuffix(lc_word[0])
        else:
            return False

    return True


def palindrome2(word):
    # lowercase the string
    lc_word = word.lower()
    # compare the original and inverted strings
    if lc_word == lc_word[::-1]:
        return True
    else:
        return False


def palindrome3(word):
    # lowercase the string
    lc_word = word.lower()

    if len(lc_word) <= 1:
        return True
    elif lc_word[0] != lc_word[-1]:
        return False
    # the recursion func checks a slice [1:-1] until the fist and last chars are not equal, then it is not a palindrome,
    # or if they are equal till a slice is one char, then it is a palindrome
    return palindrome3(lc_word[1:-1])


# print('palindrome')
# print(palindrome('шалаш'))
# a = '5двалцущуцпощзцупщцупзщцупщзцупзщо' + '5двалцущуцпощзцупщцупзщцупщзцупзщ'[::-1]
# print(palindrome(a))
# print(palindrome('ІтраванічохитаахиЛудженізоріАроматлексидійЮлфотоФлюйідискелтамораірозІнеждулихаАтихочінаварті'))
# print(palindrome(''), '\n')
#
#
# print('palindrome2')
# print(palindrome2('шалаш'))
# a = '5двалцущуцпощзцупщцупзщцупщзцупзщо' + '5двалцущуцпощзцупщцупзщцупщзцупзщ'[::-1]
# print(palindrome2(a))
# print(palindrome2('ІтраванічохитаахиЛудженізоріАроматлексидійЮлфотоФлюйідискелтамораірозІнеждулихаАтихочінаварті'))
# print(palindrome2(''), '\n')
#
#
# print('palindrome3')
# print(palindrome3('шалаш'))
# a = '5двалцущуцпощзцупщцупзщцупщзцупзщо' + '5двалцущуцпощзцупщцупзщцупщзцупзщ'[::-1]
# print(palindrome3(a))
# print(palindrome3('ІтраванічохитаахиЛудженізоріАроматлексидійЮлфотоФлюйідискелтамораірозІнеждулихаАтихочінаварті'))
# print(palindrome3(''))
