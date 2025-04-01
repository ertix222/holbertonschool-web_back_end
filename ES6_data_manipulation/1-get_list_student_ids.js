function getListStudentIds(StudentsArray) {
  if (!Array.isArray(StudentsArray)) {
    return [];
  }
  return StudentsArray.map((Student) => Student.id);
}

export default getListStudentIds;
