from classes import Library, Book, Employee, Student, Order

library1 = Library.Library('Warszawa', 'Kwiatowa',
                           '10-200', '8-20', '123456789')
library2 = Library.Library('Krakow', 'Kotlarska',
                           '40-200', '7-16', '188888889')

book1 = Book.Book(library1, '20.09.2010', 'James', 'Mcgill', '321')
book2 = Book.Book(library1, '11.11.2010', 'Arthur', 'Fresh', '366')
book3 = Book.Book(library2, '02.02.2010', 'Agatha', 'Esd', '491')
book4 = Book.Book(library2, '15.09.2020', 'Jules', 'Bin', '78')
book5 = Book.Book(library1, '20.09.2002', 'Coss', 'Sin', '100')

employee1 = Employee.Employee('Ala', 'Kowalska', '20.01.2021', '01.01.1999',
                              'Bytom', 'Kwaka', '42-600', '098765432')
employee2 = Employee.Employee('Robert', 'Kowal', '20.11.2021', '12.12.1999',
                              'Chorzow', 'Lipowa', '42-600', '088323432')
employee3 = Employee.Employee('Macej', 'Polska', '21.01.2021', '09.09.1999',
                              'T.Gory', 'Lipna', '42-600', '1424162')

student3 = Student.Student('Julia', [100, 200, 300])
student4 = Student.Student('Agnieszka', [87, 19, 20])
student5 = Student.Student('Wera', [11, 2, 54])

order1 = Order.Order(employee1, student5, [book5, book1], '20.09.2022')
order2 = Order.Order(employee2, student3, [book2, book4, book1], '12.10.2022')

print(order1)
print(order2)
