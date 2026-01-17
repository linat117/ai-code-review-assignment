# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    count = 0

    for email in emails:
        if isinstance(email, str) and "@" in email and email.strip() != "": # here i used different validatino since the first was so easy so now it checks in three ways which is reliable  enough
            count += 1

    return count