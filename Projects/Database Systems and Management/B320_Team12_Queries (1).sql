-- 1. Transcripts

SELECT 
    e.EnrolledCourseID,
    e.StudentID,
    s.FirstName,
    s.LastName,
    e.CourseOfferingID,
    c.CourseID,
    c.Title_Short_Description,
    e.GradeID,
    g.LetterGrade,
    g.Points,
    co.TermsID,
    t.AcademicYear,
    t.AcademicSemester
FROM EnrolledCourses e
LEFT JOIN Students s 
	ON s.StudentID = e.StudentID
LEFT JOIN CourseOfferings co 
	ON e.CourseOfferingID = co.CourseOfferingID
LEFT JOIN Courses c 
	ON co.CourseID = c.CourseID
LEFT JOIN AcademicTerms t 
	ON co.TermsID = t.TermsID
LEFT JOIN Grades g 
	ON e.GradeID = g.GradeID
ORDER BY s.StudentID, t.TermsID;


-- 2. Number of students by classification

SELECT 
    CASE 
        WHEN TotalCredits BETWEEN 0 AND 29 THEN 'Freshman'
        WHEN TotalCredits BETWEEN 30 AND 59 THEN 'Sophomore'
        WHEN TotalCredits BETWEEN 60 AND 89 THEN 'Junior'
		WHEN TotalCredits BETWEEN 90 AND 120 THEN 'Senior'
        ELSE 'Alumni'
    END AS Classification,
	m.MajorDescription,
    COUNT(DISTINCT ec.StudentID) AS NumberOfStudents
FROM EnrolledCourses ec
INNER JOIN Students s 
	ON ec.StudentID = s.StudentID
INNER JOIN Majors m 
	ON s.MajorID = m.MajorID
WHERE m.MajorDescription IN ('Computer Science', 'Info Science & Tech', 'Psychology')
GROUP BY 
    CASE 
        WHEN TotalCredits BETWEEN 0 AND 29 THEN 'Freshman'
        WHEN TotalCredits BETWEEN 30 AND 59 THEN 'Sophomore'
        WHEN TotalCredits BETWEEN 60 AND 89 THEN 'Junior'
		WHEN TotalCredits BETWEEN 90 AND 120 THEN 'Senior'
        ELSE 'Alumni'
    END,
	m.MajorDescription;


-- 3. Number of students who got a C or better

WITH GPA_Calculation AS (
    SELECT
        ec.StudentID,
        at.TermsID,
		m.MajorDescription,
        AVG(g.Points) AS GPA,
        CASE 
			WHEN TotalCredits BETWEEN 0 AND 29 THEN 'Freshman'
            WHEN TotalCredits BETWEEN 30 AND 59 THEN 'Sophomore'
            WHEN TotalCredits BETWEEN 60 AND 89 THEN 'Junior'
			WHEN TotalCredits BETWEEN 90 AND 120 THEN 'Senior'
            WHEN TotalCredits >= 120 THEN 'Alumni'
        END AS Classification
    FROM EnrolledCourses ec
    INNER JOIN Grades g 
		ON ec.GradeID = g.GradeID
	INNER JOIN CourseOfferings co
		ON ec.CourseOfferingID = co.CourseOfferingID
    INNER JOIN AcademicTerms at 
		ON co.TermsID = at.TermsID
    INNER JOIN Students s 
		ON ec.StudentID = s.StudentID
    INNER JOIN Majors m 
		ON s.MajorID = m.MajorID
    WHERE
        m.MajorDescription IN ('Computer Science', 'Info Science & Tech')
        AND g.LetterGrade IN ('A', 'B+', 'B', 'C+', 'C')
    GROUP BY ec.StudentID, at.TermsID, m.MajorDescription, TotalCredits
)
SELECT
    at.AcademicSemester,
    m.MajorDescription,
    Classification,
    COUNT(DISTINCT gpa.StudentID) AS StudentsCompletedWithCOrBetter
FROM GPA_Calculation gpa
INNER JOIN AcademicTerms at 
	ON gpa.TermsID = at.TermsID
INNER JOIN Majors m
	ON gpa.MajorDescription = m.MajorDescription
GROUP BY
    at.AcademicSemester,
    at.AcademicYear,
	m.MajorDescription,
    Classification
ORDER BY at.AcademicYear, at.AcademicSemester, Classification;


-- 4. All Classes offered by Department of CSCI and MATH with Completion Rates

SELECT 
    c.Course_Description,
    COUNT(CASE WHEN g.LetterGrade IN ('A', 'B+', 'C+', 'C') THEN 1 END) * 100.0 / COUNT(ec.StudentID) AS PercentageCompletedWithCOrBetter,
    COUNT(CASE WHEN g.LetterGrade NOT IN ('A', 'B+', 'C+', 'C') THEN 1 END) * 100.0 / COUNT(ec.StudentID) AS PercentageNotCompletedWithCOrBetter
FROM EnrolledCourses ec
INNER JOIN CourseOfferings co 
	ON ec.CourseOfferingID = co.CourseOfferingID
INNER JOIN Courses c 
	ON co.CourseID = c.CourseID
INNER JOIN Subjects s
	ON c.SubjectID = s.SubjectID
INNER JOIN Departments d 
	ON s.DepartmentID = d.DepartmentID
INNER JOIN Grades g 
	ON ec.GradeID = g.GradeID
WHERE d.DepartmentDescription = 'Math & Comp Sci'
GROUP BY c.Course_Description;

-- 5. Course offerings with less than 10 Students

SELECT 
    c.Course_Description,
    COUNT(ec.StudentID) AS EnrollmentCount
FROM EnrolledCourses ec
INNER JOIN CourseOfferings co 
	ON ec.CourseOfferingID = co.CourseOfferingID
INNER JOIN Courses c 
	ON co.CourseID = c.CourseID
INNER JOIN Subjects s
	ON c.SubjectID = s.SubjectID
WHERE s.DepartmentID = (
						SELECT DepartmentID 
						FROM Departments 
						WHERE DepartmentDescription = 'Math & Comp Sci'
						)
GROUP BY c.Course_Description
HAVING COUNT(ec.StudentID) < 10;

-- Since we have at least 10 students in the Math & Comp Sci Department the course offerings stay! Yippee!

-- 6. Report number of CSCI Students by GPA range

SELECT 
    CASE 
        WHEN GPA >= 4 THEN 'A'
		WHEN GPA BETWEEN 3.95 AND 4 THEN 'Summa Cum Laude'
		WHEN GPA BETWEEN 3.75 AND 3.949 THEN 'Magna Cum Laude'
		WHEN GPA BETWEEN 3.5 AND 3.749 THEN 'Cum Laude'
        WHEN GPA BETWEEN 3.5 AND 3.99 THEN 'B+'
        WHEN GPA BETWEEN 3.0 AND 3.49 THEN 'B'
        WHEN GPA BETWEEN 2.5 AND 2.99 THEN 'C+'
        WHEN GPA BETWEEN 2.0 AND 2.49 THEN 'C'
        ELSE 'Below C'
    END AS GPArange,
    COUNT(s.StudentID) AS NumberOfStudents
FROM 
    (
        SELECT 
            ec.StudentID,
            AVG(g.Points) AS GPA
        FROM EnrolledCourses ec
        INNER JOIN Students s 
			ON ec.StudentID = s.StudentID
        INNER JOIN Grades g 
			ON ec.GradeID = g.GradeID
        GROUP BY ec.StudentID
    ) AS GPA_Calculation
INNER JOIN Students s 
	ON GPA_Calculation.StudentID = s.StudentID
INNER JOIN Majors m 
	ON s.MajorID = m.MajorID
WHERE m.MajorDescription = 'Computer Science'
GROUP BY 
    CASE 
	WHEN GPA >= 4 THEN 'A'
		WHEN GPA BETWEEN 3.95 AND 4 THEN 'Summa Cum Laude'
		WHEN GPA BETWEEN 3.75 AND 3.949 THEN 'Magna Cum Laude'
		WHEN GPA BETWEEN 3.5 AND 3.749 THEN 'Cum Laude'
        WHEN GPA BETWEEN 3.5 AND 3.99 THEN 'B+'
        WHEN GPA BETWEEN 3.0 AND 3.49 THEN 'B'
        WHEN GPA BETWEEN 2.5 AND 2.99 THEN 'C+'
        WHEN GPA BETWEEN 2.0 AND 2.49 THEN 'C'
        ELSE 'Below C'
    END;


-- 7. Students on Academic Probation at end of prior semester

WITH GPA_Calculation AS (
    SELECT
        ec.StudentID,
        at.TermsID,
        AVG(g.Points) AS GPA
    FROM EnrolledCourses ec
    INNER JOIN Grades g 
		ON ec.GradeID = g.GradeID
	INNER JOIN CourseOfferings co
		ON ec.CourseOfferingID = co.CourseOfferingID
    INNER JOIN AcademicTerms at 
		ON co.TermsID = at.TermsID
    GROUP BY ec.StudentID, at.TermsID
),
Previous_GPA AS (
    SELECT
        gpa.StudentID,
        gpa.TermsID,
        gpa.GPA,
        LAG(gpa.GPA) OVER (PARTITION BY gpa.StudentID ORDER BY gpa.TermsID) AS PreviousGPA
    FROM GPA_Calculation gpa
)
SELECT
    at.AcademicSemester,
    at.AcademicYear,
    s.StudentID,
    s.FirstName,
    s.LastName,
    pg.GPA AS CurrentGPA,
    pg.PreviousGPA AS PreviousGPA
FROM Previous_GPA pg
INNER JOIN AcademicTerms at 
	ON pg.TermsID = at.TermsID
INNER JOIN Students s 
	ON pg.StudentID = s.StudentID
WHERE pg.PreviousGPA >= 2.0 AND pg.GPA < 2.0
ORDER BY at.AcademicYear, at.AcademicSemester, s.StudentID;



-- 8. Students who successfully exited academic probation

WITH GPA_Calculation AS (
    SELECT
        ec.StudentID,
        at.TermsID,
        AVG(g.Points) AS GPA
    FROM EnrolledCourses ec
    INNER JOIN Grades g 
		ON ec.GradeID = g.GradeID
	INNER JOIN CourseOfferings co
		ON ec.CourseOfferingID = co.CourseOfferingID
    INNER JOIN AcademicTerms at 
		ON co.TermsID = at.TermsID
    GROUP BY ec.StudentID, at.TermsID
),
Previous_GPA AS (
    SELECT
        gpa.StudentID,
        gpa.TermsID,
        gpa.GPA,
        LAG(gpa.GPA) OVER (PARTITION BY gpa.StudentID ORDER BY gpa.TermsID) AS PreviousGPA
    FROM
        GPA_Calculation gpa
)
SELECT
    at.AcademicSemester,
    at.AcademicYear,
    s.StudentID,
    s.FirstName,
    s.LastName,
    pg.GPA AS CurrentGPA,
    pg.PreviousGPA AS PreviousGPA
FROM
    Previous_GPA pg
INNER JOIN AcademicTerms at 
	ON pg.TermsID = at.TermsID
INNER JOIN Students s 
	ON pg.StudentID = s.StudentID
WHERE pg.PreviousGPA < 2.0 AND pg.GPA >= 2.0
ORDER BY at.AcademicYear, at.AcademicSemester, s.StudentID;

-- 9. Number of students in each program, overall gpa, academic probation, and graduates

SELECT 
    a.AcademicSemester,
    a.AcademicYear,
    m.MajorDescription,
    COUNT(DISTINCT s.StudentID) AS NumberOfStudents,
    AVG(gpa.GPA) AS OverallGPA,
    COUNT(CASE 
        WHEN gpa.GPA < 2.0 THEN 1 
        END) AS NumberOnProbation,
    COUNT(CASE 
        WHEN m.MajorDescription IN ('Computer Science', 'Info Science & Tech', 'Psychology')
            AND ec.TotalCredits > 120
            AND a.AcademicYear = '2024-01' AND a.AcademicSemester = 'Spring 2024' THEN 1
        ELSE NULL
        END) AS NumberGraduating
FROM AcademicTerms a
INNER JOIN CourseOfferings co
    ON a.TermsID = co.TermsID
INNER JOIN EnrolledCourses ec 
    ON co.CourseOfferingID = ec.CourseOfferingID
INNER JOIN Students s 
    ON ec.StudentID = s.StudentID
INNER JOIN Majors m 
    ON s.MajorID = m.MajorID
INNER JOIN 
    (
        SELECT 
            ec.StudentID,
            AVG(g.Points) AS GPA
        FROM EnrolledCourses ec
        JOIN Grades g 
            ON ec.GradeID = g.GradeID
        GROUP BY ec.StudentID
    ) AS gpa 
    ON s.StudentID = gpa.StudentID
INNER JOIN Grades g 
    ON ec.GradeID = g.GradeID
GROUP BY 
    a.AcademicSemester,
    a.AcademicYear,
    m.MajorDescription;


-- 10. List of students who have or are currently repeating courses

WITH CourseAttempts AS (
    SELECT
        ec.StudentID,
        s.FirstName,
        s.LastName,
        c.CourseID,
        c.Course_Description,
        at.AcademicSemester,
        at.AcademicYear,
        ec.GradeID,
        g.LetterGrade,
        ROW_NUMBER() OVER (PARTITION BY ec.StudentID, c.CourseID ORDER BY at.TermsID) AS AttemptNumber
    FROM EnrolledCourses ec
    INNER JOIN CourseOfferings co 
		ON ec.CourseOfferingID = co.CourseOfferingID
    INNER JOIN Courses c 
		ON co.CourseID = c.CourseID
    INNER JOIN AcademicTerms at 
		ON co.TermsID = at.TermsID
    LEFT JOIN Grades g 
		ON ec.GradeID = g.GradeID
    INNER JOIN Students s 
		ON ec.StudentID = s.StudentID
),
InitialAttempts AS (
    SELECT
        StudentID,
        FirstName,
        LastName,
        CourseID,
        Course_Description,
        AcademicSemester AS InitialSemester,
        AcademicYear AS InitialYear,
        LetterGrade AS InitialGrade,
        AttemptNumber
    FROM CourseAttempts
    WHERE AttemptNumber = 1
),
FinalAttempts AS (
    SELECT
        StudentID,
        FirstName,
        LastName,
        CourseID,
        Course_Description,
        AcademicSemester AS FinalSemester,
        AcademicYear AS FinalYear,
        CASE
            WHEN LetterGrade IS NULL THEN 'In Progress'
            ELSE LetterGrade
        END AS FinalGrade,
        AttemptNumber
    FROM CourseAttempts
    WHERE AttemptNumber > 1
)
SELECT
    i.StudentID,
    i.FirstName,
    i.LastName,
    i.Course_Description,
    i.InitialSemester,
    i.InitialYear,
    i.InitialGrade,
    f.FinalSemester,
    f.FinalYear,
    f.FinalGrade
FROM InitialAttempts i
JOIN FinalAttempts f ON i.StudentID = f.StudentID AND i.CourseID = f.CourseID
ORDER BY i.StudentID, i.Course_Description, i.InitialSemester;
