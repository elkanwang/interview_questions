/*
This file contains my attempt to solve the questions on cc
Author: Jacob Wang
*/


/*
1. the difference between implicit join and explicit join
    e.g.
    from course inner join teachers 
    on course.teacherid = teachers.teacherid

    from course, teachers
    where course.teacherid = teachers.teacherid

2. normalized and denormalized database
    normalized db minimizes redundancy, while denormalized
    db optimizes read time. Denormalization is often used
    to create highly scalable systems
*/

-- all students and how many couses each student is enrolled in

select first(studentName), count(distinct courseID)
from students left join studentCourses
on students.studentID = studentCourses.studentID
group by studentID

-- all teachers and how many students they teach
-- sort the list in descending order of # of students

/*
select
from teachers left join courses
on teachers.teacherID = courses.teacherID

select teacherID, count(studentID)
from courses, studentCourses, students
where courses.courseID = studentCourses.courseID
    and studentCourses.studentID = students.studentID
group by teacherID, courseID
*/

select teacherName, isnull(studentSize.number, 0)
from teachers left join
    (select teacherID, count(studentCourses.courseID) as [number]
     from courses inner join studentCourses
     on courses.courseID = studentCourses.courseID
     group by courses.teacherID) studentSize
on teachers.teacherID = studentSize.teacherID
order by studentSize.number desc

/*
small db design
1. handle ambiguity
2. define the core objects (entity)
3. analyze relationships (e.g. cardinality)
4. investigate actions (i.e. frequently used queries)

big db design
you must denormalize your db
*/


-- list of tenants who are renting more than one apartment

-- list of all buildings and the # of open requests

-- close all requests from apartments in building #11
update table Requests
set status = 'Close'
where AptID in (select AptID
                from Apartments
                where BuildingID = 11
                and Apt is not null);

-- what are the different types of joins

-- what is denormalization? explain the pros and cons

-- draw the E-R model of companies, ppl and professionals

-- design a db for students and provide a simple query to return
-- a list of top 10% students, sorted by their GPA

