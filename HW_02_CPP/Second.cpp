#include <stdlib.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

struct Student {
    string firstName;
    string lastName;
    int studentID;
    double GPA;
};

void printStudents(vector<Student> students) {
    for (int i=0;i<students.size();i++) {
        cout << students[i].firstName <<  endl ;
        cout << students[i].lastName << endl ;
        cout << students[i].studentID << endl  ;
        cout << students[i].GPA  << endl;
    }
};

vector<Student> addStudent(vector<Student> students) {

    Student newStudent;

    cout << "First Name: ";
    cin >> newStudent.firstName;
    cout << "Last Name: ";
    cin >> newStudent.lastName;
    cout << "ID: ";
    cin >> newStudent.studentID;
    cout << "GPA: ";
    cin >> newStudent.GPA;

    students.push_back(newStudent);

    return students;
}

vector<Student> delStudent(vector<Student> students) {
    int studentIDtoDel;
    cout << "ID of student to delete: ";
    cin >> studentIDtoDel;

    cout << "ID to delete: " << studentIDtoDel << endl;

    // object is removed from vector and same vector returned
    bool isFound = false;
    vector <Student>::iterator it3;
    for (it3 = students.begin(); it3 != students.end(); ++it3) {
        if (it3->studentID == studentIDtoDel) {
                it3 = students.erase(it3);
                --it3;
                isFound = true;
        }

    }
    if (!isFound) {
    cout << "ID # not found" << endl;
    }


    return students;
}


int main() {
    vector<Student> students;
    string input;

    while (true) {
        cout<<"Input operation: ";
        cin >> input;

        if (input == "ADD" || input == "a" || input == "add") {
            students = addStudent(students);
        }
        else if (input == "PRINT" || input == "p" || input == "print") {
            printStudents(students);
        }
        else if (input == "DELETE" || input == "d" || input == "delete") {
            students = delStudent(students);
        }
        else if (input == "QUIT" || input == "q" || input == "quit") {
            return 0;
        }
    }
}
