import re

from database1 import engine
from database1 import SessionLocal

from models import Base
from models import Student


# Create tables if not present
Base.metadata.create_all(engine)


def validate_name(name: str):
    """
    Reject names containing digits.
    """

    if any(char.isdigit() for char in name):
        raise ValueError(
            "Name cannot contain numbers."
        )

    if len(name.strip()) == 0:
        raise ValueError(
            "Name cannot be empty."
        )


def create_student():

    name = input("Enter Name: ").strip()
    roll_no = input("Enter Roll Number: ").strip()

    validate_name(name)

    if not roll_no.isdigit():
        raise ValueError(
            "Roll number must be numeric."
        )

    roll_no = int(roll_no)

    session = SessionLocal()

    try:

        existing_student = (
            session.query(Student)
            .filter(Student.roll_no == roll_no)
            .first()
        )

        if existing_student:
            raise ValueError(
                "Roll number already exists."
            )

        student = Student(
            name=name,
            roll_no=roll_no
        )

        session.add(student)

        session.commit()

        session.refresh(student)

        print(
            f"\nStudent Added Successfully "
            f"(ID={student.id})"
        )

    except Exception as e:

        session.rollback()

        print(
            f"\nError: {e}"
        )

    finally:

        session.close()


def show_students():

    session = SessionLocal()

    try:

        students = (
            session.query(Student)
            .order_by(Student.id)
            .all()
        )

        print("\n----- STUDENTS TABLE -----")

        if not students:
            print("No records found.")
            return

        print(
            f"{'ID':<5}"
            f"{'NAME':<20}"
            f"{'ROLL NO'}"
        )

        for student in students:

            print(
                f"{student.id:<5}"
                f"{student.name:<20}"
                f"{student.roll_no}"
            )

    finally:

        session.close()


def main():

    while True:

        print("\n1. Add Student")
        print("2. Show Students")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":

            create_student()

        elif choice == "2":

            show_students()

        elif choice == "3":

            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()