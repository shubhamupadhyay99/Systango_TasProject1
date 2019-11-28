import csv


class Products():

    List_Header=['Product-Name', 'Product-CostPrice', 'Country', 'Product-SalesTax', 'Product-FinalPrice']

    def tax_price(self,cost,tax):
        return int(cost) + int(cost) * (tax/100)

    def read_file(self):
        with open('productdata_tax.csv', 'r') as read_data:
            read = csv.reader(read_data)
            field = []
            next(read)
            for row in read:
                field.append([row[0],row[1],row[2],row[3],self.tax_price(row[1], int(row[3]))])
        return field


    def output_file(self):
        result = self.read_file()
        with open('Countyvise_salesTax.csv', 'w') as data:
            write = csv.writer(data)
            result.insert(0, self.List_Header)
            write.writerows(result)
        data.close()



if __name__ == "__main__":
    Products().output_file()
