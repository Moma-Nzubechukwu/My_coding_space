#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Task {
    string text;
    bool completed;
};

class TodoList {
private:
    vector<Task> tasks;

public:
    void addTask() {
        string taskText;
        cout << "Enter task: ";
        getline(cin, taskText);
        Task task = {taskText, false};
        tasks.push_back(task);
    }

    void viewTasks() {
        cout << "Tasks:" << endl;
        for (int i = 0; i < tasks.size(); i++) {
            cout << i + 1 << ". ";
            if (tasks[i].completed) {
                cout << "[X] ";
            } else {
                cout << "[ ] ";
            }
            cout << tasks[i].text << endl;
        }
    }

    void completeTask() {
        int taskNumber;
        cout << "Enter task number to complete: ";
        cin >> taskNumber;
        cin.ignore(); // ignore newline character
        if (taskNumber > 0 && taskNumber <= tasks.size()) {
            tasks[taskNumber - 1].completed = true;
        } else {
            cout << "Invalid task number." << endl;
        }
    }

    void deleteTask() {
        int taskNumber;
        cout << "Enter task number to delete: ";
        cin >> taskNumber;
        cin.ignore(); // ignore newline character
        if (taskNumber > 0 && taskNumber <= tasks.size()) {
            tasks.erase(tasks.begin() + taskNumber - 1);
        } else {
            cout << "Invalid task number." << endl;
        }
    }
};

int main() {
    TodoList todoList;
    while (true) {
        cout << "1. Add task" << endl;
        cout << "2. View tasks" << endl;
        cout << "3. Complete task" << endl;
        cout << "4. Delete task" << endl;
        cout << "5. Quit" << endl;
        int choice;
        cin >> choice;
        cin.ignore(); // ignore newline character
        switch (choice) {
            case 1:
                todoList.addTask();
                break;
            case 2:
                todoList.viewTasks();
                break;
            case 3:
                todoList.completeTask();
                break;
            case 4:
                todoList.deleteTask();
                break;
            case 5:
                return 0;
            default:
                cout << "Invalid choice." << endl;
        }
    }
    return 0;
}

