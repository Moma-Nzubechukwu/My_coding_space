#include <iostream>
#include <string>
#include <map>

using namespace std;

class Book {
public:
    string title;
    string author;
    string status;

    Book(string title, string author) {
        this->title = title;
        this->author = author;
        this->status = "Available";
    }
};

class Library {
private:
    map<string, Book> books;

public:
    void addBook(string title, string author) {
        Book book(title, author);
        books[title] = book;
        cout << "Book added successfully." << endl;
    }

    void removeBook(string title) {
        if (books.find(title) != books.end()) {
            books.erase(title);
            cout << "Book removed successfully." << endl;
        } else {
            cout << "Book not found." << endl;
        }
    }

    void borrowBook(string title) {
        if (books.find(title) != books.end()) {
            if (books[title].status == "Available") {
                books[title].status = "Borrowed";
                cout << "Book borrowed successfully." << endl;
            } else {
                cout << "Book is already borrowed." << endl;
            }
        } else {
            cout << "Book not found." << endl;
        }
    }

    void returnBook(string title) {
        if (books.find(title) != books.end()) {
            if (books[title].status == "Borrowed") {
                books[title].status = "Available";
                cout << "Book returned successfully." << endl;
            } else {
                cout << "Book is already available." << endl;
            }
        } else {
            cout << "Book not found." << endl;
        }
    }

    void displayBooks() {
        for (auto& book : books) {
            cout << "Title: " << book.second.title << endl;
            cout << "Author: " << book.second.author << endl;
            cout << "Status: " << book.second.status << endl;
            cout << endl;
        }
    }
};

int main() {
    Library library;

    while (true) {
        cout << "Library Management System" << endl;
        cout << "1. Add book" << endl;
        cout << "2. Remove book" << endl;
        cout << "3. Borrow book" << endl;
        cout << "4. Return book" << endl;
        cout << "5. Display books" << endl;
        cout << "6. Exit" << endl;

        int choice;
        cin >> choice;

        switch (choice) {
            case 1: {
                string title, author;
                cout << "Enter book title: ";
                cin.ignore();
                getline(cin, title);
                cout << "Enter book author: ";
                getline(cin, author);
                library.addBook(title, author);
                break;
            }
            case 2: {
                string title;
                cout << "Enter book title: ";
                cin.ignore();
                getline(cin, title);
                library.removeBook(title);
                break;
            }
            case 3: {
                string title;
                cout << "Enter book title: ";
                cin.ignore();
                getline(cin, title);
                library.borrowBook(title);
                break;
            }
            case 4: {
                string title;
                cout << "Enter book title: ";
                cin.ignore();
                getline(cin, title);
                library.returnBook(title);
                break;
            }
            case 5:
                library.displayBooks();
                break;
            case 6:
                return 0;
            default:
                cout << "Invalid choice." << endl;
        }
    }

    return 0;
}

