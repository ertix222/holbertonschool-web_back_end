function getStudentIdsSum(StdIdSum) {
  if (!Array.isArray(StdIdSum)) {
    return 0;
  }
  return StdIdSum.reduce((sum, student) => sum + student.id, 0);
}

export default getStudentIdsSum;
