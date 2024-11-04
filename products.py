import pandas
import pandas.io.formats
import pandas.io.formats.excel 

class ProductsDocument():

    def __init__(self, document_path):
        self.document_path = document_path
        pandas.io.formats.excel.ExcelFormatter.header_style = None
    
    def read(self):
        excel_file = pandas.ExcelFile(self.document_path)
        self.sheet_name = excel_file.sheet_names[0]
        self.data = excel_file.parse(self.sheet_name)
    
    def get_products_from_file(self):
        self.read()
        product_list = []
        for index, row in self.data.iterrows():
            product_list.append({"ID наши" : int(row["ID наши"]), "ID ozon" : int(row["ID ozon"])})
        
        return product_list
    
    def write_prices_to_file(self, product_list, path = None):
        if not path:
            path = self.document_path
        for index, product in enumerate(product_list):
            for column in product:
                self.data.loc[index, column] = product[column]
        writer = pandas.ExcelWriter(path)
        self.data.to_excel(writer, index=False, sheet_name = self.sheet_name)
        worksheet = writer.sheets[self.sheet_name]
        format = writer.book.add_format({"font_name": "Arial"})
        worksheet.set_column('A:Z', None, format)
        worksheet.set_row(0, None, format)
        writer.close()