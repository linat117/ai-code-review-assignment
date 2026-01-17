# AI Code Review Assignment (Python)

## Candidate
- Name: Hilina Teshome
- Approximate time spent: 70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- It divides by total number of orders (len(orders)) instead of the number of orders that are not cancelled.
- It will crash if all orders are cancelled or if its empty

### Edge cases & risks
- empty list of orders that is zer division error
- missing of "amount" or "status" key may cause KeyError

### Code quality / design issues
-  accessing the dictionary(order["amount"]) directly is not  safe. and the logic assumes all of the orders have status and amount , which might fail at some cases.

## 2) Proposed Fixes / Improvements
### Summary of changes
- count only non cancelled orders
-use .get() on orders to safely access the dictionary keys.
-Return 0 if there are no valid orders found so it avoid division by zero.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
-Test wit both cancelled and non cancelled orders to see the output on both cases.
-test with empty list
-test with a missing amount or status keys to check keyError.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Assumes the average si correct but it's divided by total orders not the valid only.
-No consideration of cases like empty list or if all orders are cancelled.

### Rewritten explanation
- This function calculates teh average value of non calculated orders. It sums teh amount of each order where status is not cancelled and it divides by the number of such orders. If tehre are no valid orders , it will return 0 and missing amount  fields also be treated as 0.

## 4) Final Judgment
- Decision: Approve 
- Justification: The corrected code now handles edge cases, calculate average correctly and is safe
- Confidence & unknowns: High confidence 

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- -Original code only checks for @ so it may count invalid emails like empty string or None

### Edge cases & risks
- Empty list of  email should return 0
-emails that are None or empty strings
-Non strings could raise exceptions

### Code quality / design issues
- There is no type checking (isinstance ) for safety
-teh validation is too simple which may miss invalid email entries.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added type check
-Ignore empty string and string having spaces
-Count only string that have @

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
-List containing valid emails, invalid emails, empty strings, None, numbers.
-Empty list of emails.
-Emails with whitespace or malformed strings.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Claims to safel  ignore invalid entried but the original code crashed on None and it also counts empty ones

### Rewritten explanation
- This function counts the number of valid email addresses in a list. A valid email is a non-empty string containing "@". Invalid entries, including None or empty strings, are ignored. The function safely handles empty input and avoids errors from non-string values.

## 4) Final Judgment
- Decision: Approve 
- Justification:the Corrected code now counts valid emails and handle edge cases safely.
- Confidence & unknowns: High confidence on the input being a list

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- It divides by total number of entries, including None
- Crashes if the list is empty 

### Edge cases & risks
- Input list empty
-Mixed types like strings that can't be converted to float

### Code quality / design issues
- No error handling mainly for types
-It assumes all values can be converted to float

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only valid measurements 
-Use try/except to safely skip invalid entries.
-Return 0 if there are no valid measurements.

Corrected code

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
-Empty list
-List with valid numbers, strings that are numbers, and invalid strings

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Claims to safely handle mixed types, but original code crashes if any value cannot convert to float.
- Divides by total length, not valid count.

### Rewritten explanation
-This function calculates the average of valid measurements in a list. It ignores None values and any entries that cannot be converted to float. If there are no valid measurements, it returns 0 to prevent division by zero. This ensures a safe and accurate average for mixed input types. 

## 4) Final Judgment
- Decision: Approve 
- Justification:Corrected code handles invalid type, empty list and None safely. and the average calculation is accurate now.
- Confidence & unknowns: High confidence
