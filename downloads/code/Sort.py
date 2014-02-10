#!--
#ChooseSort


class Sort(list):
    def __init__(self, list):
        self.list = list

    def swap(self, i, j):
        list[i], list[j] = list[j], list[i]

    def show(self):
        print " ".join(str(v) for v in list)

    def select_sort(self):
        for i in range(0, len(list)-1):
            min = i
            for j in range(i+1, len(list)):
                if list[j] < list[min]:
                    min = j
            self.swap(min, i)
        return list

    def insert_sort(self):
        for i in range(1, len(list)):
            temp = list[i]
            j = i-1
            while j >= 0 and temp < list[j]:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = temp

    def quick_sort(self, low=0, high=None):
        if high == None:
            high = len(list) - 1
        if low < high:
            s, i, j = list[low], low, high
            while True:
                while i != high and list[i] < s:
                    i = i + 1
                # if i < j:
                #     list[i] = list[j]
                #     i = i + 1
                while j !=low and list[j] > s:
                    j = j - 1
                # if i < j:
                #     list[j] = list[i]
                #     j = j - 1
                if i < j:
                    list[j], list[i] = list[i], list[j]
                else:
                    break
            list[j], s = s, list[j]
            self.quick_sort(low, i - 1)
            self.quick_sort(i + 1, high)

    def bubble_sort(self):
        for i in range(len(list) - 1, 0, -1):
            for j in range(0, i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == "__main__":
    list = [6, 4, 1, 9, 2, 7, 10, 3]
    print 'select_sort'
    s = Sort(list)
    s.select_sort()
    s.show()

    list = [6, 4, 1, 9, 2, 7, 10, 3]
    print 'insert_sort'
    s = Sort(list)
    s.insert_sort()
    s.show()

    list = [6, 4, 1, 9, 2, 7, 10, 3]
    print 'quick_sort'
    s = Sort(list)
    s.quick_sort(0, len(list)-1)
    s.show()

    list = [6, 4, 1, 9, 2, 7, 10, 3]
    print 'bubble_sort'
    s = Sort(list)
    s.bubble_sort()
    s.show()
