import csv 


def insertion_sort(arr, simulation=False):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr

new_csv=[]
count = 0
with open('./cs_combined_toner.csv', 'r' ) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader : 
        count += 1
        print(count)
    
        for cell in row : 
            if "product_name" in cell.split(" "): 
                new_csv.append([count, cell])
        # new_row = insertion_sort(row)
        # print(new_row)
        # new_csv.append(new_row)


with open( './cs_combined_done.csv' , 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    for i in new_csv:
        writer.writerow(i)

