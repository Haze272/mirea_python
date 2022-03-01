class naive:
    def string_array_to_int(string_list=['5', '-2', '1990']):
        list2 = []
        for i in range(len(string_list)):
            t = int(string_list[i])
            list2.append(t)

        print(list2)

    def arr_uni_elem(list=[5, -2, 1990, 5, 0, 2, 2001, 2001]):
        unique_elem = []

        for elem in list:
            if elem in unique_elem:
                continue
            else:
                unique_elem.append(elem)
        print(unique_elem)

    def arr_reverse(list=[5, -2, 1990, 5, 0, 2, 2001, 2001]):
        for i in range(len(list) // 2):
            list[i], list[-i - 1] = list[-i - 1], list[i]

        print(list)

    def sieve(x = 5, list=[5, -2, 1990, 5, 0, 2, 2001, 2001]):



class advanced:
    def arr_reverse(list=[5, -2, 1990, 5, 0, 2, 2001, 2001]):
        new_list = list[::-1]

        print(new_list)


if __name__ == '__main__':
    naive.string_array_to_int()
    naive.string_array_to_int(['2', '2', '8'])

    naive.arr_uni_elem()

    naive.arr_reverse()
    advanced.arr_reverse()
