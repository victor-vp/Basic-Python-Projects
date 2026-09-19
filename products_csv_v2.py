import csv

def writing():
    f = open('products.csv', 'a+', newline='')   # append + read
    writer = csv.writer(f)

    while True:
        a = int(input('Enter product ID: '))
        b = input('Enter product name: ')
        c = int(input('Enter product quantity: '))
        d = int(input('Enter product price: '))
        
        m = [a, b, c, d]
        writer.writerow(m)   # write the record

        ans = input('Do you want to continue? (Y/N): ')
        if ans.lower() == 'n':
            break

    # Reset pointer to start for reading
    f.seek(0)
    reader = csv.reader(f)
    print("All Products:")
    for row in reader:
        print(row)

    f.close()
