function updateStudentGradeByCity(students, city, newGrades) {
  const stdGrade = students.filter((student) => student.location === city);

  return stdGrade.map((student) => {
    const GradeFound = newGrades.find((grade) => grade.studentId === student.id);
    return {
      ...student,
      grade: GradeFound ? GradeFound.grade : 'N/A',
    };
  });
}

export default updateStudentGradeByCity;
