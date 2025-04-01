function getStudentByLocation(StdLoc, city) {
  if (!Array.isArray(StdLoc)) {
    return [];
  }
  return StdLoc.filter((student) => student.location === city);
}

export default getStudentByLocation;
