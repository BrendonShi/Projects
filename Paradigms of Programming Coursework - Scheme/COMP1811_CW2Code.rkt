;;Name: Brendon Shymanskyi
;;Student ID: 001419181
;;Month of Birth: January

;; Data format: Name, Mother, Father, Date of birth, Date of death.
;; An empty list means Unknown.

;; Maternal branch
(define Mb
  '(((Mary Blake) ((Ana Ali) (Theo Blake)) ((17 9 2022) ()))
    ((Ana Ali) ((Ada West) (Md Ali)) ((4 10 1995) ()))
    ((Theo Blake) ((Mary Jones) (Tom Blake)) ((9 5 1997) ()))
    ((Greta Blake) ((Mary Jones) (Tom Blake)) ((16 3 1999) ()))
    ((Mary Jones) (() ()) ((12 5 1967) (19 5 2024)))
    ((Tom Blake) (() ()) ((17 1 1964) ()))
    ((Ada West) (() ()) ((22 8 1973) ()))
    ((Md Ali) (() ()) ((14 2 1972) (2 5 2023)))
    ((Ned Bloom) (() ()) ((23 4 2001) ()))
    ((John Bloom) ((Greta Blake) (Ned Bloom)) ((5 12 2023) ()))))

;; Paternal branch
(define Pb
  '(((John Smith) ((Jane Doe) (Fred Smith)) ((1 12 1956) (3 3 2021))) 
    ((Ana Smith) ((Jane Doe) (Fred Smith)) ((6 10 1958) ()))
    ((Jane Doe) ((Eve Talis) (John Doe)) ((2 6 1930) (4 12 1992)))
    ((Fred Smith) ((Lisa Brown) (Tom Smith)) ((17 2 1928) (13 9 2016)))
    ((Eve Talis) (() ()) ((15 5 1900) (19 7 1978)))
    ((John Doe) (() ()) ((18 2 1899) (7 7 1970)))
    ((Lisa Brown) (() ()) ((31 6 1904) (6 3 1980)))
    ((Tom Smith) (() ()) ((2 8 1897) (26 11 1987)))
    ((Alan Doe) ((Eve Talis) (John Doe)) ((8 9 1932) (23 12 2000)))
    ((Mary Doe) (() (Alan Doe)) ((14 4 1964) ()))))

;;------|Helper Functions|------;;

;; function to display names
(define (display-name name)
  (display (string-append (symbol->string (car name)) " " (symbol->string (cadr name))))  ; сonverts the first two elements of the list from symbols to strings and making a space between them
  (newline))

;; filter-and-display
(define (filter-and-display lst filter-members message)
  ; defining a variable 'filtered'; stores a result
  ; the 'filter' function applies 'filter-members' to each element of list and keeps only the necessary elements.
  (let ((filtered (filter filter-members lst)))
    (if (null? filtered)
        (display (string-append "No " message " found.\n")) ; if empty - no 'message' found.
        (begin 
          (display (string-append message ":\n"))
          (display-names filtered)))))

;; compare dates (year, month, day)
(define (date<? date1 date2)
  (or (< (caddr date1) (caddr date2))  ; compare years
      (and (= (caddr date1) (caddr date2))  ; if years are equal - compare months
           (or (< (cadr date1) (cadr date2))
               (and (= (cadr date1) (cadr date2))  ; if months are equal - compare days
                    (< (car date1) (car date2)))))))

;; removes duplicates | recursive function
(define (remove-duplicates lst)
  (if (null? lst)  ; base case: returns empty list if it's empty
      '()
      (cons (car lst)  ; includes the first emelent of the list in the result of the next line
            (remove-duplicates (filter (lambda (x) (not (equal? x (car lst)))) (cdr lst))))))  ; recursive case: process the rest

;;------|Main Functions|------;;10

;; C1, C2, C3:
(define (display-names lst)
  ; displaying all people in the given list or combined lists
  (for-each (lambda (entry) (display-name (car entry))) lst))

;; ------------------------

;; A1: Function to display parents from a given list
(define (parents lst)
  (let ((parent-names
         (remove-duplicates
          (append (map caadr lst)  ; extract mothers
                  (map cadadr lst)))))  ; extract fathers
    (filter-and-display
     lst
     (lambda (entry)
       (member (car entry) parent-names))  ; checks if is a parent
     "Parents in maternal branch")))

;; A2: Function to filter and display living members
(define (living-members lst)
  (filter-and-display
   lst
   (lambda (entry) (null? (cadr (caddr entry))))  ; checks if member is alive
   "Living members"))  ; message to display

;; A3: Current age (living members only)
(define (current-age lst)
  (let ((current-year 2025))
    (for-each
     (lambda (entry)
       (let* ((dob-info (car (caddr entry)))   ; extract date of birth
              (dod-info (cadr (caddr entry)))  ; extract date of death
              (birth-year (caddr dob-info)))  ; birth year
         (when (null? dod-info)  ; only show for living members
           (display 
            (string-append 
             (symbol->string (caar entry))  ; First name
             " "
             (symbol->string (cadar entry))  ; Last name
             ": "
             (number->string (- current-year birth-year))
             "\n")))))
     lst)))

;; A4: Function to find members with birthdays in October
(define (same-birthday-month lst month)
  (filter-and-display
   lst
   (lambda (entry) (= (cadr (car (caddr entry))) month))  ; checks birthday month
   "Members with birthdays in October"))  ; message

;; A5: Function to sort members by last name
(define (sort-by-last lst)
  (let ((sorted (sort lst
                       (lambda (a b)
                         (string<? (symbol->string (cadr (car a)))  ; comparing last names
                                   (symbol->string (cadr (car b))))))))
    (display "Sorted members by last name:\n")
    (display-names sorted)))

;; A6: Function to change "John" to "Juan" recursively in any list structure
(define (change-name-to-Juan lst old-name new-name)
  ; helper function to update the name if it matches 'old-name'
  (define (update-name name)
    (if (eq? (car name) old-name) (cons new-name (cdr name)) name))  ; combining with new name if the old name not matches
  ; helper to update an entry
  (define (update-entry entry)
    (cons (update-name (car entry)) (cdr entry)))  ; update the new part of the entry
  (let ((updated (map update-entry lst))) ; map: applies update-entry to each entry in lst.
    (display "Updated list with 'John' changed to 'Juan':\n")
    (display-names updated)))

;; ------------------------

;; B1: Display all children from list
(define (children lst)
  (filter-and-display
   lst
   (lambda (entry)
     ; Check if the person has at least one parent (mother or father)
     (and (not (null? (cadr entry)))
          ; checks whether mother or father exists
          (or (not (null? (caadr entry)))
               (not (null? (cadadr entry))))))
   "Children"))

;; B2: Function to find the oldest living member
(define (oldest-living-member lst)
  ; Filter the list to include only living members (those with no date of death)
  (let ((alive-members (filter (lambda (entry) (null? (cadr (caddr entry)))) lst)))
    (if (null? alive-members)
        (display "No living members found.\n")
        ; If living members exist, find the oldest and sort by date of birth (oldest first)
        (let ((oldest (car (sort alive-members (lambda (a b) (date<? (car (caddr a)) (car (caddr b))))))))
          (display "Oldest living member: ")
          (display-name (car oldest))))))

;; B3: Function to calculate average age at death
(define (average-age-on-death lst)
  ; Filter the list to include only deceased members (those with a date of death)
  (let ((deceased (filter (lambda (entry) (not (null? (cadr (caddr entry))))) lst)))
    (if (null? deceased)
        (display "No deceased members found.\n")
        ; If deceased members exist, calculate the average age at death. Map over deceased members to calculate their age at death.
        (let ((total-age (apply + (map (lambda (entry) (- (caddr (cadr (caddr entry))) (caddr (car (caddr entry))))) deceased))))
          (display "Average age at death: ")
          (display (/ (exact->inexact total-age) (length deceased))) ;; Dividing the total age by the number of deceased members
          (newline)))))

;; B4: Function to find members with birthdays in January
(define (birthday-month-same lst month)
  ; Use filter-and-display to filter members with birthdays in the month of January.
  (filter-and-display lst
                      ; Lambda function to check if the member's birth month matches the month of January.
                      (lambda (entry) (= (cadr (car (caddr entry))) month)) "Members with birthdays in January"))

;; B5: Sort members by first name
(define (sort-by-first lst)
  ; Sort the list by first name in ascending order using included comparison function
  (let ((sorted (sort lst (lambda (a b) (string<? (symbol->string (caar a)) (symbol->string (caar b)))))))
    (display "Sorted members by first name:\n")
    (display-names sorted)))

;; B6: Change "Mary" to "Maria"
(define (change-name-to-Maria lst old-name new-name)
  ; Helper function to update the name if it matches 'old-name'
  (define (update-name name)
    ; Check if the first name matches 'old-name'. And replace an old name with a new name.
    (if (eq? (car name) old-name) (cons new-name (cdr name)) name))
  ; Helper function to update an entry
  (define (update-entry entry)
    ; Update the name              | Keep the rest unchanged
    (cons (update-name (car entry)) (cdr entry)))
  (let ((updated (map update-entry lst))) ; map
    (display "Updated list with 'Mary' changed to 'Maria':\n")
    (display-names updated)))

;;------|Command Functions|------;;

(define (display-menu)
  (display "\nAvailable commands:\n")
  (display "1. Display members from Maternal Branch.\n")
  (display "2. Display members from Paternal Branch.\n")
  (display "3. Display members from both branches.\n")
  (display ">Tasks A:\n4. Display all parents in the Maternall branch.\n")
  (display "5. Display all Living members from Maternal branch.\n")
  (display "6. Display current age of all people alive.\n")
  (display "7. Display members with birthdays in October.\n")
  (display "8. Display sorted people by last name in Maternal branch.\n")
  (display "9. Change all John names to Juan.\n")
  (display ">Tasks B:\n10. Display all children from Paternal branch.\n")
  (display "11. Display the oldest living member.\n")
  (display "12. Calculate average age at death.\n")
  (display "13. Display members with birthdays in January.\n")
  (display "14. Sort members by first name.\n")
  (display "15. Change all Mary names to Maria.\n")
  (newline)
  (display "Enter command number: "))

(define (command-loop)
  (let loop ()
    (display-menu)
    (let ((input-command (read)))
      (if (not (number? input-command))
          (begin
            (display "Invalid command! Try again.\n")
            (loop))
          (cond
            ((= input-command 1) (display-names Mb)) ; C1
            ((= input-command 2) (display-names Pb)) ; C2
            ((= input-command 3) (display-names (append Mb Pb))) ; C3
            ((= input-command 4) (parents Mb)) ; A1
            ((= input-command 5) (living-members Mb)) ; A2
            ((= input-command 6) (current-age (append Mb Pb))) ; A3
            ((= input-command 7) (same-birthday-month (append Mb Pb) 10)) ; A4
            ((= input-command 8) (sort-by-last Mb)) ; A5
            ((= input-command 9) (change-name-to-Juan (append Mb Pb) 'John 'Juan)) ; A6
            ((= input-command 10) (children Pb)) ; B1
            ((= input-command 11) (oldest-living-member Pb)) ; B2
            ((= input-command 12) (average-age-on-death Pb)) ; B3
            ((= input-command 13) (birthday-month-same (append Mb Pb) 1)) ; B4
            ((= input-command 14) (sort-by-first Pb)) ; B5
            ((= input-command 15) (change-name-to-Maria (append Mb Pb) 'Mary 'Maria)) ; B6
            (else (display "Invalid command! Try again.\n"))))
      (loop))))


(command-loop)