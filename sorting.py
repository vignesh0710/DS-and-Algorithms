input_array = [21,4,1,3,9,20,25,6,21,14]


class sorting(object):

    def bubble_sort(self,input_array):

        k = 0
        while k <len(input_array):

            for i in range(len(input_array)-1):
                if input_array[i] > input_array[i+1]:
                    input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
            k  = k +1

        return input_array

s1 = sorting()
print (s1.bubble_sort(input_array))

